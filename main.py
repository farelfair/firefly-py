import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token in .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# required intents
intents = discord.Intents.default()
intents.message_content = True

# commands bot
client = commands.Bot(command_prefix = '!', intents=intents, help_command=None)

# make bot online
@client.event
async def on_ready():
    print("bot ready online")
    print("================")
    
    activity = discord.Game(name="Firefly.gg | !help")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Custom activity sudah di-set!")

# Load commands from folder
@client.event
async def setup_hook():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")

# run bot
client.run(TOKEN)
