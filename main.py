from flask import Flask, request
from telegram import Bot, Update
import os


echo_app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)


@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hi from Husniddin'

    elif request.method == 'POST':
        data = request.get_json(force=True)

        update: Update = Update.de_json(data, bot)

        chat_id = update.message.chat.id
        text = update.message.text

        if text != None:
            bot.send_message(chat_id, text)

        return 'hello'