import sys
import os
import random
import asyncio
import json

from openai import OpenAI

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from env import *

class charAIBot(discord.Client):
    """Meet charAI"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.client = None
        self.persistent_thread = None
        self.user_threads  = {}
        
    ### Helper Functions ###

    async def get_answer(self, client, run, thread):
        """Queries OpenAI to generate a response"""
        while not run.status == "completed":
            print("Waiting for answer...")
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            await asyncio.sleep(1)
        messages = client.beta.threads.messages.list(thread.id)
          
        try:
            answer = messages.data[0].content[0].text.value
        except Exception as e:
            print(e)
            answer = "I'm having trouble connecting to OpenAI. Maybe there's no spending budget left this month? Check back later!"
                
        return answer
    
    def save_server_thread(self):
        """Saves the server thread ID to a JSON file."""
        with open('.utils/server_thread.json', 'w') as file:
            json.dump({'persistent_thread_id': self.persistent_thread.id}, file)

    def load_server_thread(self):
        """Loads the server thread ID from a JSON file."""
        if os.path.exists('.utils/server_thread.json'):
            with open('.utils/server_thread.json', 'r') as file:
                data = json.load(file)
                thread_id = data.get('persistent_thread_id')
                if thread_id:
                    self.persistent_thread = self.client.beta.threads.retrieve(thread_id)

    def load_user_threads(self):
        """Loads user thread IDs from a JSON file."""
        if os.path.exists('.utils/user_threads.json'):
            with open('.utils/user_threads.json', 'r') as file:
                self.user_threads = json.load(file)
        else:
            self.user_threads = {}

    def save_user_threads(self):
        """Saves user thread IDs to a JSON file."""
        with open('.utils/user_threads.json', 'w') as file:
            json.dump(self.user_threads, file)
            
    ### Main Logic ###
            
    async def on_ready(self):
        """Triggered when the bot is ready."""
        print(f'Logged in as {self.user} (ID: {self.user.id})')

        # Setup persistent OpenAI client and thread. The bot will remember previous communication inside the server.
        self.client = OpenAI(
            organization=env_openai_organization_id,
            project=env_openai_project_id,
            api_key=env_openai_apikey
        )
        
        # Check if an OpenAI server thread already exists - This is created the first time the bot runs on a server.
        if os.path.exists('.utils/server_thread.json'):
            self.load_server_thread()
        else:
            self.persistent_thread = self.client.beta.threads.create()
            self.save_server_thread()
        
        self.load_user_threads()
            
    async def send_dm(self, user, message):
        """Sends a direct message to the specified user."""
        try:
            async with user.typing():
                # Simulate typing for a random duration between 1 and 5 seconds
                await asyncio.sleep(random.uniform(1, 5))
                await user.send(message)
        except discord.HTTPException as e:
            print(f"Failed to send DM to {user.name}: {e}")

    async def on_message(self, message):
        """Responds to direct messages & mentions with an AI generated response."""
        
        # Ignore messages from bots
        if message.author.bot:
            return
        
        # AI Response for DMs
        if message.guild is None:
            user_id = str(message.author.id)
            content = message.content.strip()

            # Check if a thread exists for the user, if not create one
            if user_id not in self.user_threads:
                thread = self.client.beta.threads.create()
                self.user_threads[user_id] = thread.id
                self.save_user_threads()
            else:
                thread_id = self.user_threads[user_id]
                thread = self.client.beta.threads.retrieve(thread_id)
            
            # Send the message to OpenAI for response generation
            user_message = self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=content
            )
            
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=env_openai_assistant_id,
            )
            
            answer = await self.get_answer(self.client, run, thread)
            
            async with message.channel.typing():
                # Simulate typing for a random duration between 5 and 10 seconds
                await asyncio.sleep(random.uniform(5, 10))
                await message.channel.send(answer)
        
        # AI Response for mentions
        if self.user in message.mentions:
            # Extract the message content and include user and channel info
            content = message.content.replace(f'<@!{self.user.id}>', env_bot_name).strip()
            username = message.author.name
            channel_name = message.channel.name
            
            # Create the contextual content
            contextual_content = f"User {username} in channel {channel_name} says: {content}"
            
            # Using the server-wide persistent thread
            thread = self.persistent_thread
            
            # Build the message to send to OpenAI
            user_message = self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=contextual_content
            )
            
            # Send the message to OpenAI for response generation
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=env_openai_assistant_id,
            )
            
            answer = await self.get_answer(self.client, run, thread)
            async with message.channel.typing():
                # Simulate typing for a random duration between 5 and 10 seconds
                await asyncio.sleep(random.uniform(5, 10))
                await message.channel.send(answer)

    async def close(self):
        await super().close()
        await self.http.close()

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = charAIBot(intents=intents)

client.run(env_token)