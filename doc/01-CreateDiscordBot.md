# Step 01 - Create the Discord Bot

## Navigate to the Discord Developer portal
[https://discord.com/developers](https://discord.com/developers)

## Create the bot
![Image01](img/01/01.png?raw=true)

- Click "New Application"%
- Insert the bots name, as it should appear in the discord user list
- Read and accept the Developer TOS and Developer Policy
- Click "Create"

## Configure the bot

### General Information Menu
![Image02](img/01/02.png?raw=true)

- Add an App Icon
- Add a description
- Save changes

### OAuth2 Menu
![Image03](img/01/03.png?raw=true)
- Click "Add Redirect"
- Insert the following URL: https://discordapp.com/oauth2/authorize?&client_id=[CLIENT_ID]&scope=bot
- substitute `[CLIENT_ID]` with your actual client ID
- Save changes

Take note of that link! You will need it to invite the bot to your discord server.

### Bot Menu
#### Token
Click `Reset Token` and follow the On-Screen instructions. Note the new token, as this cannot be displayed again.
The token goes into the `env_token` variable in `env.py` 

#### Autorization flow
- Uncheck Public Bot

#### Privileged Gateway Intents
- Check Server Members Intent
- Check Message Content Intent

- Save changes

## Done
- The Discord part of the configuration is done