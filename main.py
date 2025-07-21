import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import gemini
from keep_alive import keep_alive


load_dotenv()

client = discord.Client(intents=discord.Intents.all())
my_token = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.', intents=discord.Intents.default())
players = {}


async def process(message):
    print(message)
    print(message.content)
    response = gemini.generate_content(message.content)
    await message.channel.send(response)
            


@client.event
async def on_ready():
    #await client.change_presence(status=discord.Status.idle,
    #                             activity=discord.Streaming(
    #                                 name='GeoGuessr',
    #                                 url='https://www.geoguessr.com/'))
    print('Ich bin {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    else:
        await process(message)

keep_alive()

try:
    client.run(my_token)
except:
    os.system("kill 1")
