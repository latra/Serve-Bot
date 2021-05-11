from utils.constants import *
import os
import requests
import json
import logging

lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
url = os.getenv("SERVER_URL")
game = ""
bot_ip = os.getenv("BOT_API")
async def terraria(ctx):
    await ctx.send(lang_string[TERRARIA_ASKED])
    logging.info(f"Enviando petición a {url}")
    game = "terraria"
    request_body = {
        'server_uid':ctx.guild.id,
        'game':game,
        'action':'serve',
        'callback_url': bot_ip,
        'channel_uid': ctx.channel.id,
        'callbackurl': url}

    try:
        x = requests.post(url, data = request_body, headers= {'token':os.getenv("API_TOKEN")})
        if x.status_code == 200:
            await ctx.send(lang_string[TERRARIA_ASKED])
        elif x.status_code == 403:
            await ctx.send(lang_string[TERRARIA_ERROR_FORBBIDEN])
        elif x.status_code == 440:
            await ctx.send(lang_string[TERRARIA_ERROR_RUNNING])
    except TimeoutError as ex:
        await ctx.send(lang_string[SERVER_COMUNICATION_ERROR])
