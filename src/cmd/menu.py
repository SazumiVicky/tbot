"""
- dev: Sazumi Viki
- ig: @moe.sazumiviki
- gh: github.com/sazumivicky
- site: https://sazumi.moe
"""

from src.handler import cmd_files
from telethon.sync import events
import importlib

async def handle(event, client):
    if hasattr(event.message, 'to_id'):
        username = await client.get_entity(event.message.sender_id)
        username = username.username if username.username else "User"

        menu_text = f"Halo {username} ada yang bisa Viki bantu ? Berikut menu yang tersedia untuk saat ini:\n\n"

        for cmd_file in cmd_files:
            cmd_module = importlib.import_module(f"src.cmd.{cmd_file}")
            if hasattr(cmd_module, "cmd_info"):
                cmd_info = cmd_module.cmd_info
                menu_text += f"{cmd_info['category']}\n{cmd_info['cmd']}\n\n"

        await client.send_message(event.message.to_id, menu_text)
    else:
        print("Oops something went wrong")

cmd_info = {
    "cmd": "/menu",
    "help": "menu /none",
    "category": "main",
    "owner": False
}