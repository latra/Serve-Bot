from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import request
import asyncio
from discord.ext import commands as discord_commands
import nest_asyncio
import logging
from dotenv import load_dotenv
import sys, os
        
class BotApi: 
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.token = os.getenv('DISCORD_TOKEN')
        @self.app.route('/game', methods = ['POST'])
        def gameServer():
            body_json = request.json
            asyncio.run(self.game_response(body_json))
            print(request)

            return 'OK'
    async def game_response(self, body_json):
        await self.treatment(body_json['server_uid'], body_json['channel_uid'], body_json['game'], body_json['status'], body_json['ip'], body_json['port'])
    async def treatment(self, server_uid, channel_uid, game, status, ip, port):

        client = discord_commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))
        @client.event
        async def on_ready():
            print("Aqui sigue!!!!!!!!")

            print("channel: " + channel_uid)
            channel = client.get_channel(channel_uid)
            await channel.send('test')
            exit()
        print("Aqui llega!!!!!!!!")
        nest_asyncio.apply()
        __import__('IPython').embed()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(self.token))
    def start(self):
        
        print("STARTING!")
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
