from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 24033868
api_hash = "564ad1f71b6ee36b1e2eb7eeb98b5b9f"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Here is your STRING_SESSION:")
    print(client.session.save())
