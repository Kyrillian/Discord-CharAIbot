# Step 04 - Usage

## Interacting with the bot
By default the bot is configured to respond to any DMs, as well as @mentions or Replies in any channels of your discord it can read.


## Bot 'conscious'
Upon boot the bot creates `.utils/server_thread.json` This is a persistent reference to the Assistants chat thread (think chats in ChatGPT).
If this file already exists (e.g. on any subsequent boot) it will read form the file and use the same thread.
This leads to the bot 'remembering' past conversations and being able to reference them - Up to the maximum context amount configured in the GPT model.
Along with the message, the bot gets context data about who sent the message and in what channel. That way the bot can differentiate between different users.

Aside from this "server-wide" conscious the bot possesses unique consciouses for DM interactionsd with each user.
These are stored in `.utils/user_threads.json`, again linking user_id's to thread id's.
The conscious in a DM conversation is not aware of anything being said on the server or in DMs with other users.

## Done
Congratulations! Your bot should be logged in.