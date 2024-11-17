# Simsimi Chatbot Integration with Facebook Messenger

> **⚠️ Note:**  
> **This project is an old project created while I was learning programming.**  
> The code does not follow modern best practices and may need refactoring.  
> It serves as a learning example and is not maintained according to current standards.  
> **However, it still works as expected.**

This project integrates Simsimi's chatbot API with Facebook Messenger using the `fbchat` library. It listens for incoming messages in a Facebook chat and replies with a generated response from Simsimi.

## Features

- Integration with the Simsimi API for conversational responses.
- Facebook Messenger bot that automatically replies to messages.
- Simple setup with `fbchat` library.
- Echo bot functionality that responds with Simsimi's generated text.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `fbchat`
  - `requests`

You can install the required libraries by running:

  ```bash
  pip install fbchat requests
```
## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/EthicalYuu/simsimi-chatbot-integration.git

2. Navigate into the project directory:
   ```bash
   cd simsimi-chatbot-integration

3. Install the required dependencies:
   ```bash
   pip install fbchat requests

4. Open the script and replace the following:

    * Simsimi API Key: Replace "API-1234-abcd-1234-abcd" with your Simsimi API key.
    * Facebook Credentials: Replace "example@example.com" with your Facebook username/email, and "password123" with your Facebook password.

5. Run the bot:
    ```bash
    python bot.py
    ```
    The bot will log into your Facebook account and start listening for messages.

## How It Works

1. Login to Facebook: The bot logs into your Facebook account using your credentials.
2. Listening for Messages: It listens for incoming messages in a chat thread.
3. Sending a Reply: When it detects a message from another user, it uses the Simsimi API to generate a response and sends it back to the thread.
4. The bot responds to messages that are not from itself, echoing a reply from the Simsimi chatbot.

## Example of the Flow

1. User sends a message to the bot.
2. The bot fetches a response from the Simsimi API.
3. The bot replies in the same thread with the generated response.

## Future Enhancements

- Refactor the code and securely store Facebook credentials: The current code could benefit from optimization and improvements in structure and design, and avoid hardcoding credentials, as it was written early in my programming journey.
- Add support for handling multiple threads.
- Improve error handling for API failures.
- Add advanced conversation management (e.g., context awareness).
- Allow for custom responses based on user input.
