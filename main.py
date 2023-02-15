from flask import Flask, request

echo_app = Flask(__name__)

@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hi from Husniddin'
    elif request.method == 'POST':
        data = request.get_json(force=True)
        # data = {
        #     'update_id': 366164406, 
        #     'message': {
        #         'message_id': 151, 
        #         'from': {'id': 1258594598, 'is_bot': False, 'first_name': 'Diyorbek', 'last_name': 'Jumanov', 'username': 'jumanovdiyorbek', 'language_code': 'en'}, 
        #         'chat': {'id': 1258594598, 'first_name': 'Diyorbek', 'last_name': 'Jumanov', 'username': 'jumanovdiyorbek', 'type': 'private'}, 
        #         'date': 1676463994, 
        #         'text': '/start', 
        #         'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}
        #         ]
        #     }
        # }

        chat_id = data['message']['from']['id']
        text = data['message']['text']

        print(chat_id, text)
        return 'hello'

if __name__ == '__main__':
    echo_app.run()