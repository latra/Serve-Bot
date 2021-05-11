from dotenv import load_dotenv
from utils.constants import *
import logging
import sys, os
import json
from multiprocessing import Process

import discord
from discord.ext import commands as discord_commands
from discord.ext.commands import CommandInvokeError

import commands.help as HelpCommand
from commands.serve import ServeCommand
from commands.stop import StopCommand
class DiscordBot:
    def __init__(self):
        lang_string = json.load(open(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'src/bot/strings/ES-es.json')))
        logging.info(os.getenv('DISCORD_PREFIX'))
        
        logging.info("Reading bot config data")

        intents = discord.Intents.all()

        self.client = discord_commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))
        self.token = os.getenv('DISCORD_TOKEN')
        self.index = 0
        self.client.remove_command('help')
        logging.info("Reading bot functions")

        @self.client.command()
        async def help(ctx):
            await HelpCommand.help(ctx)
            
        @self.client.command()
        async def serve(ctx):
            message_words = ctx.message.content.split(' ')
            if len(message_words) > 1:
                if message_words[1] == 'terraria':
                    await ServeCommand().terraria(ctx)
            else:
                await ctx.send(lang_string[UNKNOWN_COMMAND])

        @self.client.command()
        async def terraria(ctx):
            await ServeCommand().terraria(ctx)            
        @self.client.command()
        async def stop(ctx):
            message_words = ctx.message.content.split(' ')
            if len(message_words) > 1:
                if message_words[1] == 'terraria':
                    await StopCommand().terraria(ctx)
            else:
                await ctx.send(lang_string[UNKNOWN_COMMAND])
        @self.client.event
        async def on_command_error(ctx, error):
            if isinstance(error, discord_commands.CommandError):
                if isinstance(error, CommandInvokeError):
                    logging.error(error)
                    await ctx.send(lang_string[BOT_ERROR])
                else:
                    logging.error(error)
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
