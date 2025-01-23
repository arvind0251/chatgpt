import requests
import os

# Load Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")  # OR replace with your token: "your-bot-token"

# API URL to check bot status
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("ok"):
        print(f"✅ Bot is Active! Username: @{data['result']['username']}")
    else:
        print("❌ Bot is NOT Active! Check the bot token.")
except Exception as e:
    print(f"⚠️ Error: {e}")
