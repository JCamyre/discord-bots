import os 

import discord 
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	# Pass in a function to search through the guilds the bot is in
	guild = discord.utils.get(client.guilds, name=GUILD) # This is the current guild/server the bot is in
 
	# This is for developers to see what server our bot is connected to via the console
	print(f'{client.user} has connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})')

	members = "\n - ".join(sorted([member.name for member in guild.members]))
	print(f'All members in alphabetical order:\n - {members}')

client.run(TOKEN)
