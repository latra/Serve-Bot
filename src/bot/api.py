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
        self.client = discord_commands.Bot(command_prefix="")
        self.token = os.getenv('DISCORD_TOKEN')
        @self.client.event
        async def on_ready():
            self.app = Flask(__name__)
            self.api = Api(self.app)
            @self.app.route('/game', methods = ['POST'])
            def gameServer():
                body_json = request.json
                self.treatment(body_json['server_uid'], body_json['channel_uid'], body_json['game'], body_json['status'], body_json['ip'], body_json['port'], body_json['password'])
                return '200 OK'

            self.app.run(host="0.0.0.0", port='4030')
            
        self.client.run(self.token)

    def treatment(self, server_uid, channel_uid, game, status, ip, port, password):
        if status == 200:
            message = lang_string[TERRARIA_READY].format(IP=ip, PORT=port, PASSWORD=password)
        else:
            message = lang_string[BOT_ERROR]

        channel = client.get_channel(channel_uid)
        asyncio.run(channel.send(message))
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading env configuration")
    if len(sys.argv) != 1:
        load_dotenv(sys.argv[1])
    else:
        load_dotenv()
    api = BotApi()
    api.start()
