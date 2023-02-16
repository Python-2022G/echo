from flask import Flask, request
# from telegram import Bot, Update
import os


echo_app = Flask(__name__)

# TOKEN = os.environ['TOKEN']
# bot = Bot(TOKEN)


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
        chat_id = data['message']['chat']['id']
        text = data['message']['text']

        print(chat_id, text)

        return 'hello'
