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


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.reply("☄ Blahaj Shower 🦈")
    await client.process_commands(message)


@client.command()
async def blahaj(ctx):
    def random_blahaj():
        with open('blahaj.json') as dt:
            data = json.load(dt)
            random_index = random.randint(0, len(data) - 1)
            return data[random_index]["url"], data[random_index]["name"]

    blahajImageLink, blahajImageName = random_blahaj()
    embed = discord.Embed(
        description=f"Here is a **{blahajImageName}** 🦈", color=discord.Color.from_rgb(178, 208, 250))
    embed.set_image(url=blahajImageLink)
    await ctx.reply(embed=embed)


client.run(TOKEN)
