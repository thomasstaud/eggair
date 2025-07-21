import main
from discord.ext import commands
import os
from dotenv import load_dotenv
import gemini


load_dotenv()

client = main.Client(intents=main.Intents.all())
my_token = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.', intents=main.Intents.default())
players = {}


async def process(message):
    response = gemini.generate_content(message)
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
