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

        print(data)

        return 'hello'