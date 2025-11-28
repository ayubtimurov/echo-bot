from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()



TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Start command recieved!")
    await update.message.reply_text("Thanks for starting Echo Bot!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Help command recieved!")
    await update.message.reply_text("I am an Echo bot. Please type something, so I can repeat it.")


# Responses

def handle_response(text: str) -> str:
    return f"{text}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")




if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=2)
