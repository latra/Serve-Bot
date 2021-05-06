from dotenv import load_dotenv
from utils.constants import *
import logging
import sys, os
import json
from multiprocessing import Process

import discord
from discord.ext import commands as discord_commands

import commands.help as HelpCommand
import commands.serve as ServeCommand 
class DiscordBot:
    def __init__(self):
        lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
        logging.info(os.getenv('DISCORD_PREFIX'))
        
        logging.info("Reading bot config data")


        self.client = discord_commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'), guild_subscriptions=True, self_bot=False)
        self.token = os.getenv('DISCORD_TOKEN')
        self.index = 0
        self.client.remove_command('help')
        logging.info("Reading bot functions")
        @self.client.command()
        async def help(ctx):
            await HelpCommand.help(ctx)
        @self.client.command()
        async def terraria(ctx):
            await ServeCommand.terraria(ctx)
        @self.client.command()
        async def stop(ctx):
            pass
        @self.client.event
        async def on_command_error(ctx, error):
            value = ''.join(traceback.format_exception(None, error, error.__traceback__))
            logging.error(value)
            if isinstance(error, discord_commands.CommandError):
                from src.modules.commands.utils import CatchedError
                logging.error(error)
                if isinstance(error, CommandInvokeError) and isinstance(error.original, CatchedError):
                    await ctx.send(lang_string[BOT_ERROR])
                else:
                    await ctx.send(lang_string[UNKNOWN_COMMAND])
            else:
                raise error

    def start(self):
        logging.info("Starting bot!")
        self.client.run(self.token)
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading env configuration")
    if len(sys.argv) != 1:
        load_dotenv(sys.argv[1])
    else:
        load_dotenv()
    bot = DiscordBot()
    bot.start()
