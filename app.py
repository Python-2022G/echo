from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

from main import (
    start,
    echo,
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

        dispatcher: Dispatcher = Dispatcher(bot, None, workers=0)
        update: Update = Update.de_json(data, bot) # create an update obj
        
        dispatcher.add_handler(CommandHandler('start', callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text, echo))
        
        dispatcher.process_update(update)
        
        return 'hello'
