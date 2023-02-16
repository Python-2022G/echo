from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    
    # send msg
    bot.send_message(chat_id, 'WELCOME TO OUR BOT!')

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text)