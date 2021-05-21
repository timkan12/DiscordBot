import discord
from discord.ext import commands
import json


from apikey import *
client = commands.Bot(command_prefix = "!")

intents = discord.Intents.default()
intents.members = True

@client.event
async def on_ready():
    print('hello')

@client.command()
async def discord_test(ctx):
    await ctx.send("test1")

@client.event
async def on_vc_join(member):
    channel = client.get_channel(702220092825534524)
    await channel.send('Later nerd')

@client.command(pass_context = True)
async def join_Me(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Sike, you must be in voice channel to cast command loser!')

@client.command(pass_context = True)
async def leave_Me(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('ight peace!')
    else:
        await ctx.send('Not in a VC, cannot leave')

client.run(token)
