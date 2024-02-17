# Telegram Bot

This Telegram bot is built using Telethon and is designed to handle various commands. The bot has a modular structure, where each command is defined in a separate Python file in the `src/cmd` directory.

## Commands

Here's a list of available commands:

- `/menu`: Displays a list of all available commands. The bot will greet the user and provide a list of commands in an easy-to-read format.
- `/ping`: The bot will respond with a message "Pong!".

## Setup and Usage

1. Copy the `.env.example` file to a new file named `.env`.
2. Fill in `API_ID` and `API_HASH` in the `.env` file with your Telegram API details.
3. Run the bot with the command `python main.py`.

## Adding New Commands

To add a new command, follow these steps:

1. Create a new Python file in the `src/cmd` directory. For example, `src/cmd/hello.py`.
2. Inside this file, define a `handle` function that will be called when the command is received. This function should take two arguments: `event` and `client`.
3. Inside the `handle` function, you can write the logic to handle the command.
4. Define a `cmd_info` dictionary that contains details about the command. This should include a `cmd` key that specifies the command text, and can also include other keys such as `help` and `category`.

Here's an example of a new command:

```python
async def handle(event, client):
    await client.send_message(event.message.to_id, "Hello, world!")

cmd_info = {
    "cmd": "/hello",
    "help": "Sends a 'Hello, world!' message",
    "category": "main",
    "owner": False
}
```
