from telegram import Update
from telegram.ext import CallbackContext, Updater


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to our bot!')


def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text)

