import os
from telethon.sync import TelegramClient

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
channel = os.getenv("CHANNEL_NAME")

client = TelegramClient("anon", api_id, api_hash)

with client:
    messages = client.iter_messages(channel, limit=100)
    with open("sub.txt", "w", encoding="utf-8") as f:
        for message in messages:
            if message.text and "vless" in message.text:  # فیلتر بر اساس کلمه
                f.write(message.text + "\n")
