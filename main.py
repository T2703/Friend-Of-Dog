from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, File
from discord.ext import tasks
import discord
import os

# This gets the token.
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)

# How to send in the friend of dog.
@tasks.loop(hours=24)
async def sendDaily():
    channel = client.get_channel(813952721065082974) 
    if channel:
        await channel.send(file = discord.File('gorpcore.jpg'))

# HANDLING THE STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')
    sendDaily.start()

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
