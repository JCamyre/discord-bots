import os 

import discord 
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD: # This is the current guild/server the bot is in
			break
	# This is for developers to see what server our bot is connected to via the console
	print(f'{client.user} has connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})')

	members = guild.members
	

client.run(TOKEN)
