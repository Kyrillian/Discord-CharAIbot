# Step 02 - Create the OpenAI Assistant

## Navigate to the OpenAI API Platform
[https://platform.openai.com/](https://platform.openai.com/)

## Create a project
![Image01](img/02/01.png?raw=true)

- Mouseover your default Project
- Click "Create Project"
- Choose a name for the Project and click "Create"

## Create a budget (!)
OpenAI API calls are not free. It is highly reccomended that you create a budget for your project as a safeguard against unforeseen cost.

![Image02](img/02/02.png?raw=true)

- Click on the Cog icon in the top-right corner
- Navigate to "Projects" -> "Limits"
- Click "Set budget"
- Set your budget and save it.

## Create the Assistant
![Image03](img/02/03.png?raw=true)

- Navigate to [https://platform.openai.com/assistants](https://platform.openai.com/assistants)
- Make sure your created Project is selected
- Click "Create Assistant"

![Image04](img/02/04.png?raw=true)

### Name
This is the name for your assistant. What you put here has no bearing on the behavior or identity of the chatbot.

### Instructions
This is the meat of the assistant. What you put here molds the identity of the character. The more detailed the description the better - at the cost of more credits expended.
ChatGPT can help in engineering a fitting prompt.

With "Einsteinbot", I used the following prompt:
`I need you to come up with a system prompt for an OpenAI Assistant. This assistant should believe he is Albert Einstein, act in a way consistent with his character and have his personality and knowledge. It is imperative that the assistant never drops the facade.`

### Model
Choose the GPT model to use for the chatbot. More advanced models command a higher usage fee per token.
Please refer to the OpenAI pricing chart found here: [https://openai.com/api/pricing/](https://openai.com/api/pricing/)

Take note of the assistant ID, this goes into the `env_openai_assistant_id` variable in `env.py` 

## Create an API key
Navigate to "API keys" in the left hand menu bar and click on "Create new secret key"
Have the secret key owned by a service account and click "Create secret key".
Take note of the key - this cannot be displayed again.
The API key goes into the `env_openai_apikey` variable in `env.py` 

![Image05](img/02/05.png?raw=true)

## Finalize env.py
Insert the two missing env_ variables into env.py.

Your organization ID can be found using the cog icon in the top-right corner and navigating to "Organization" -> "General".
Your project ID can be found in the same menu under "Project" -> "General". Make sure you have the correct project selected.

## Done
- The OpenAI part of the configuration is done