from discord.ext import commands
import discord
from discord import File
import bot_functions
import os
from time_converter import TimeConverter

client = commands.Bot(command_prefix='.')
functions = bot_functions.BotFunctions()
time_conv = TimeConverter()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')


@client.command()
async def b(ctx):
    await ctx.send(functions.all_todays_bosses())

@client.command()
async def jutro(ctx):
    await ctx.send(functions.all_tomorrows_bosses())

@client.command()
async def nastepny(ctx):
    await ctx.send(functions.todays_next_boss())

@client.command(aliases = [time_conv.command_function()])
async def _komenda(ctx):
    await ctx.send("Bossy info\n", file=File("files\\files\\important\\modulators\\pictures\\67769093_647195719101937_5634612662714236928_n.jpg"))

client.run("KAROLEK TUTAJ WPISZ KOD DO SWOJEGO KANALU")


