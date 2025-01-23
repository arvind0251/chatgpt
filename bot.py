import telebot
import openai
import os
from flask import Flask, request

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Initialize Telegram Bot
bot = telebot.TeleBot(BOT_TOKEN)

# Flask App for Webhook
app = Flask(__name__)

@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(func=lambda message: True)
def chat_with_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response["choices"][0]["message"]["content"])
    except Exception as e:
        bot.reply_to(message, "Error: " + str(e))

# Start Flask server
@app.route('/')
def index():
    return "ChatGPT Bot is Running!"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://your-heroku-app-name.herokuapp.com/" + BOT_TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
