# Step 01 - Create the Discord Bot

### Navigate to the Discord Developer portal
[https://discord.com/developers](https://discord.com/developers)

### Create the bot
![Image01](img/01/01.png?raw=true)

- Click "New Application"

General Information Menu
App Icon
Name
Description



Save Changes

OAuth2 Menu
Add Redirect
https://discordapp.com/oauth2/authorize?&client_id=`[CLIENT ID]`&scope=bot
Paste Client ID

Save Changes

Bot Menu
Under Autorization flow
Uncheck Public Bot

Under privileged Gateway Intents
Check Server Members Intent
Check Message Content Intent

Save Changes