from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import request
        
class BotApi: 
    def __init__(self, client):
        self.client = client
        self.app = Flask(__name__)
        self.api = Api(self.app)
        @self.app.route('/game', methods = ['POST'])
        async def gameServer():
            body_json = request.json
            channel = self.client.get_channel(body_json['channel_uid'])
            await channel.send('test')
            return "all ok!"
    def start(self):
        print("STARTING!")
        self.app.run(host="0.0.0.0", port='4030')
