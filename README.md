# Discord-CharAIbot

CharAIbot is a Discord bot leveraging the OpenAI Assistant functionality to create a chatbot that behaves in a way you configure it to.

## Features

- Responds to mentions in channels
- Responds to DMs
- persistent consciousness of conversations up to the maximum amount of context configured in the AI model

## Branches

- `main`    : productive branch, latest stable release
- `dev`     : dev branch, Work-in-Progress

## OpenAI

CharAIbot uses an OpenAI assistant to respond to mentions and DMs with AI generated texts.

Threads are persistent, with DMs and server interaction using seperate conciousnesses.
Mentions in the server share a persistent consciousness, whereas each users DM-interactions use their own.

`.utils/user_threads.json` : holds an array linking each user id to an OpenAI thread for DM interation.
`.utils/server_thread.json`: holds a single OpenAI thread id for in-server interaction.

These files are created and maintained automatically and locally.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- A Discord bot created and configured in the Discord developer portal (free)
- An OpenAI Assistant configured in the OpenAI API portal (paid)
- Creativity!

### Documentation

This boilerplate requires parameterization of the `env.py` file.
To get the base functionality running, the following env_ variables need to be provided:

- env_token :  Your bot token from the discord developer portal
- env_bot_name :  The name the bot would use to refer to itself
- env_openai_assistant_id : Your Assistant ID from the OpenAI API portal
- env_openai_apikey : An API key to the OpenAI API with permission to make API calls
- env_openai_organization_id : Your OpenAI organization ID
- env_openai_project_id : The project ID of your OpenAI Assistant

A step-by-step guide, from creating the discord bot, to creating the Assistant all the way to parameterizing and running bot.py is provided in the `doc` folder.

## Acknowledgements

- The Suck Up! game community for inspiring the creation of this project.
- The developers of discord.py for their fantastic library.

## Contact

For any questions or problems, please open an issue.

