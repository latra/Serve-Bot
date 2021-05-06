from utils.constants import *
import os
import strings
import json

lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))

async def help(ctx):
    await ctx.send(lang_string[HELP])
    