from utils.constants import *
import os
import requests
import json

lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
url = os.getenv("SERVER_URL")
game = ""
bot_ip = os.getenv("BOT_API")
async def terraria(ctx):
    await ctx.send(lang_string[TERRARIA_ASKED])
    game = "terraria"
    request_body = {'server_uid':ctx.guild.id , 'game':game, 'callback_url': bot_ip}
    await ctx.send("DUMMY MESSAGE. BACKEND NOT RUNNING")

    # x = requests.post(url, data = request_body, headers= {'token':os.getenv("API_TOKEN")})
    # if x.status_code == 200:
    #     await ctx.send(lang_string[TERRARIA_TRUE])
    # elif x.status_code == 403:
    #     await ctx.send(lang_string[TERRARIA_ERROR_FORBBIDEN])
    # elif x.status_code == 440:
    #     await ctx.send(lang_string[TERRARIA_ERROR_RUNNING])