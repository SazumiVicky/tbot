"""
- dev: Sazumi Viki
- ig: @moe.sazumiviki
- gh: github.com/sazumivicky
- site: https://sazumi.moe
"""

from telethon.sync import TelegramClient
from src import handler
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

session_file = "./src/session"
client = TelegramClient(session_file, api_id, api_hash)

if __name__ == "__main__":
    handler.setup_handlers(client)
    client.start()
    client.run_until_disconnected()