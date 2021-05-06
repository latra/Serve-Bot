from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import request
import asyncio

        
class BotApi: 
    def __init__(self, client, token):
        self.client = client
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
        @self.client.event
        async def on_ready():
            print("channel: " + channel_uid)
            channel = self.client.get_channel(channel_uid)
            await channel.send('test')
            exit()
        self.client.run(self.token)
    def start(self):
        
        print("STARTING!")
        self.app.run(host="0.0.0.0", port='4030')
