
import os
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to handle messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text

    # Call OpenAI's GPT-4 model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response['choices'][0]['message']['content']
    update.message.reply_text(bot_reply)

# Function to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm a GPT-4 powered bot. How can I assist you today?")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
