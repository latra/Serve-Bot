from utils.constants import *
import os
import requests
import json
import logging

class ServeCommand:
    def __init__(self):
        self.lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
        self.url = os.getenv("SERVER_URL")
        self.game = ""
        self.bot_ip = os.getenv("BOT_API")
        self.api_token = os.getenv("API_TOKEN")
    async def terraria(self, ctx):
        await ctx.send(self.lang_string[TERRARIA_ASKED])
        logging.info(f"Enviando petición a {self.url}")
        self.game = "terraria"
        request_body = {
            'server_uid':ctx.guild.id,
            'game': self.game,
            'action':'serve',
            'callback_url': self.bot_ip,
            'channel_uid': ctx.channel.id}

        try:
            x = requests.post(self.url, data = request_body, headers= {'token':self.api_token})
            if x.status_code == 200:
                await ctx.send(self.lang_string[TERRARIA_ASKED])
            elif x.status_code == 403:
                await ctx.send(self.lang_string[TERRARIA_ERROR_FORBBIDEN])
            elif x.status_code == 440:
                await ctx.send(self.lang_string[TERRARIA_ERROR_RUNNING])
        except TimeoutError as ex:
            await ctx.send(self.lang_string[SERVER_COMUNICATION_ERROR])
