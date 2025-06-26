import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os

URL = "https://t.me/s/🔗_کانال_تو_"  # ← اینو با کانالت عوض کن

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")
messages = soup.find_all("div", class_="tgme_widget_message_text")

subs = []

for msg in messages:
    text = msg.get_text()
    if any(proto in text for proto in ["vmess://", "vless://", "trojan://", "ss://", "http://", "https://"]):
        subs.append(text.strip())

os.makedirs("public", exist_ok=True)

with open("public/sub.txt", "w", encoding="utf-8") as f:
    if subs:
        f.write("\n\n".join(subs))
    else:
        f.write("# No subscription links found today\n")

print(f"[{datetime.now()}] Saved {len(subs)} links to public/sub.txt")
