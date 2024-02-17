"""
- dev: Sazumi Viki
- ig: @moe.sazumiviki
- gh: github.com/sazumivicky
- site: https://sazumi.moe
"""

async def handle(event, client):
    await client.send_message(event.message.to_id, "Pong!")

cmd_info = {
    "cmd": "/ping",
    "help": "none",
    "category": "main",
}
