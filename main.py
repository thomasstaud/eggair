import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import gemini
from keep_alive import keep_alive


load_dotenv()

my_token = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True 
client = commands.Bot(command_prefix='.', intents=intents)

user_conversations = {}

async def process(message):
    
    user_id = message.author.id
    username = message.author.display_name # Oder message.author.name für den Nutzernamen ohne Spitznamen
    current_user_history = user_conversations.get(user_id)
    
    # Übergib den Benutzernamen an die gemini.generate_content-Funktion
    response_text, updated_history = gemini.generate_content(message.content, current_user_history, username)
    user_conversations[user_id] = updated_history
    await message.channel.send(response_text)

@client.event
async def on_ready():
    print(f'Ich bin {client.user} und bereit!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return

    await client.process_commands(message)
    await process(message)

keep_alive()

try:
    client.run(my_token)
except Exception as e:
    print(f"Error starting bot: {e}")