from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, CommandHandler, Filters
import os

from main import (
    start,
    echo
)

app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hi from Python-2022I'

    elif request.method == 'POST':
        data = request.get_json(force=True) # get data from request

        update: Update.de_json(data, bot)

        dp: Dispatcher = Dispatcher(bot, None, workers=0)  # dispatcher   
        
        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update) # process update
        return 'hello'
