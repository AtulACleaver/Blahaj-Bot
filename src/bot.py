import discord
from discord import player
from discord import colour
from discord.ext import commands
from discord.ext.commands.errors import BadArgument, CommandNotFound, MissingRequiredArgument
import random
import json

with open('config.json', 'r') as f:
    config = json.load(f)
TOKEN = config['token']

client = commands.Bot(command_prefix="-", help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="-help"))
    print("We Are Ready Now")


@client.command()
async def hello(ctx):
    await ctx.reply("Hey!")

client.run(TOKEN)
