from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import request
import asyncio
from discord.ext import commands as discord_commands
import nest_asyncio
        
class BotApi: 
    def __init__(self, token):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.token = token
        @self.app.route('/game', methods = ['POST'])
        def gameServer():
            body_json = request.json
            asyncio.run(self.game_response(body_json))
            print(request)

            return 'OK'
    async def game_response(self, body_json):
        await self.treatment(body_json['server_uid'], body_json['channel_uid'], body_json['game'], body_json['status'], body_json['ip'], body_json['port'])
    async def treatment(self, server_uid, channel_uid, game, status, ip, port):

        client = discord_commands.Bot(command_prefix='!serveCall')
        @client.event
        async def on_ready():
            print("channel: " + channel_uid)
            channel = client.get_channel(channel_uid)
            await channel.send('test')
            exit()
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(self.token))

    def start(self):
        
        print("STARTING!")
        self.app.run(host="0.0.0.0", port='4030')
