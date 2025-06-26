from telethon.sync import TelegramClient
import re
from datetime import datetime, timedelta
import os

api_id = 123456
api_hash = 'abcd1234abcd1234abcd1234abcd1234'
channel_username = 'نام_کانال_شما'

link_patterns = ['vmess://', 'vless://', 'trojan://', 'ss://', 'http']

client = TelegramClient('session', api_id, api_hash)

output_file = 'public/sub.txt'

def extract_links(text):
    pattern = r'(vmess://[^\s]+|vless://[^\s]+|trojan://[^\s]+|ss://[^\s]+|https?://[^\s]+)'
    return re.findall(pattern, text)

with client:
    all_links = []
    for msg in client.iter_messages(channel_username, limit=100):
        if msg.text:
            links = extract_links(msg.text)
            all_links.extend(links)

    all_links = list(set(all_links))

    os.makedirs('public', exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for link in all_links:
            f.write(link + '\n')

    print(f"{len(all_links)} لینک ذخیره شد.")