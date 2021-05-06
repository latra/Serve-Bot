from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from utils.constants import *

from flask import request
import asyncio
from discord.ext import commands as discord_commands
import nest_asyncio
import logging
from dotenv import load_dotenv
import sys, os
import json


lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
        
class BotApi: 
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.token = os.getenv('DISCORD_TOKEN')
        @self.app.route('/game', methods = ['POST'])
        def gameServer():
            body_json = request.json
            self.game_response(body_json)
            print(request)
            return '200 OK'
    def game_response(self, body_json):
         self.treatment(body_json['server_uid'], body_json['channel_uid'], body_json['game'], body_json['status'], body_json['ip'], body_json['port'], body_json['password'])
    def treatment(self, server_uid, channel_uid, game, status, ip, port, password):
        asyncio.set_event_loop(asyncio.new_event_loop())

        client = discord_commands.Bot(command_prefix="")
        @client.event
        async def on_ready():
            if status == 200:
                message = lang_string[TERRARIA_READY].format(IP=ip, PORT=port, PASSWORD=password)
            else:
                message = lang_string[BOT_ERROR]

            channel = client.get_channel(channel_uid)
            await channel.send(message)
            await client.close()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(self.token))


    def start(self):
        self.app.run(host="0.0.0.0", port='4030')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading env configuration")
    if len(sys.argv) != 1:
        load_dotenv(sys.argv[1])
    else:
        load_dotenv()
    api = BotApi()
    api.start()
