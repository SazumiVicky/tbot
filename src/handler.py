"""
- dev: Sazumi Viki
- ig: @moe.sazumiviki
- gh: github.com/sazumivicky
- site: https://sazumi.moe
"""

from telethon.sync import events
import importlib.util
import os

cmd_dir = "./src/cmd"
cmd_files = [
    f[:-3] for f in os.listdir(cmd_dir) if f.endswith(".py") and f != "__init__.py"
]


def setup_handlers(client):
    print("COMMANDS DETECTED\n")
    print("{:<10} {:<10} {:<10}".format('CMD', 'CATEGORY', 'HELP'))
    print("-" * 30)

    for cmd_file in cmd_files:
        cmd_module = importlib.import_module(f"src.cmd.{cmd_file}")
        if hasattr(cmd_module, "cmd_info") and hasattr(cmd_module, "handle"):
            cmd_info = cmd_module.cmd_info
            cmd_pattern = cmd_info["cmd"]
            cmd_handle = cmd_module.handle
            print("{:<10} {:<10} {:<10}".format(cmd_pattern, cmd_info.get("category", "None"), cmd_info.get("help", "None")))
            client.add_event_handler(
                handle_command(cmd_handle, cmd_pattern, cmd_info, client)
            )
    print("\n")


def handle_command(cmd_handle, cmd_pattern, cmd_info, client):
    async def handler(event):
        if hasattr(event, "message") and hasattr(event.message, "message"):
            message_text = event.message.message
            if message_text.startswith(cmd_pattern):
                await cmd_handle(event, client)

    return handler
