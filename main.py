from flask import Flask, request
from telegram import Bot, Update
import os


echo_app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)


@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hi from Python-2022I'

    elif request.method == 'POST':
        data = request.get_json(force=True) # get data from request
        # {
        #     'update_id': 366164447, 
        #     'message': {
        #         'message_id': 225, 
        #         'from': {'id': 1258594598, 'is_bot': False, 'first_name': 'Diyorbek', 'last_name': 'Jumanov', 'username': 'jumanovdiyorbek', 'language_code': 'en'}, 
        #         'chat': {'id': 1258594598, 'first_name': 'Diyorbek', 'last_name': 'Jumanov', 'username': 'jumanovdiyorbek', 'type': 'private'}, 
        #         'date': 1676521987, 
        #         'text': 'salom'
        #         }
        # }

        update: Update = Update.de_json(data, bot)
        
        chat_id = update.message.chat_id
        text = update.message.text

        if text != None:
            bot.send_message(chat_id, text)

        print(chat_id)
        
        return 'hello'
