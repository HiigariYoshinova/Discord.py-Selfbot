import time, os
import discord
from threading import Thread
from discord.ext import commands
from colorama import Fore
from flask import Flask


TOKEN = ""

client = commands.Bot(command_prefix="$", self_bot=True)
client_id = "989336095319789648"


#app = Flask('')

#@app.route('/')
#def home():
#    return "I'm alive"

#def run():
#  app.run(host='0.0.0.0',port=8080)

#def keep_alive():  
#    t = Thread(target=run)
#    t.start()


@client.event
async def on_connect():
    print('Logging in...')

@client.event
async def on_ready():
    os.system('clear')
    print('Logged in as', client.user)

@client.event
async def on_message(message):
    print(f'[{message.author}]', message.content)
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"**API: `{round(client.latency * 1000)}ms`**")

#keep_alive()
client.run(TOKEN, reconnect=True)
