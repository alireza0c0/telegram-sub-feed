import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

# آدرس کانال در حالت نمای عمومی
URL = "https://t.me/testconfigwithvpn"

# دریافت HTML صفحه کانال
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# پیدا کردن تمام پیام‌ها
messages = soup.find_all("div", class_="tgme_widget_message_text")

# فیلتر کردن پیام‌هایی که لینک سابسکرایب دارند
subs = []
for msg in messages:
    text = msg.get_text()
    if any(proto in text for proto in ["vmess://", "vless://", "trojan://", "ss://", "http://", "https://"]):
        subs.append(text.strip())

# ساخت پوشه docs اگر وجود نداشت
os.makedirs("docs", exist_ok=True)

# نوشتن در فایل خروجی
with open("docs/sub.txt", "w", encoding="utf-8") as f:
    if subs:
        f.write("\n\n".join(subs))
    else:
        f.write("# No subscription links found today\n")

print(f"[{datetime.now()}] Saved {len(subs)} subscription messages to docs/sub.txt")
