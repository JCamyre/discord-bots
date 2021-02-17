import os 
import re 
import sys 

from discord.ext import commands
import discord

from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default() # "Due to an API change Discord is now forcing developers who want member caching to explicitly opt-in to it. This is a Discord mandated change and there is no way to bypass it. In order to get members back you have to explicitly enable the members privileged intent and change the Intents.members attribute to true."
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD) # bot.guilds[0] == GUILD

	print(
		f'{bot.user} has connected to Discord!\n'
		f'{guild.name}(id: {guild.id})'
	)

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send( # send a message in the member's dm
		f'yo {member.name}'
	)

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return 

	# yo
	# yo = re.compile(r'\byo\b')

	# if yo.search(message.content): 
	# 	await message.channel.send('yo') # In that message's channel, send response


@bot.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f: # append to file
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}. Error: {sys.exc_info()}\n')
		else:
			raise # If any other error besides on_message, raise the error so we see it in the console

@bot.command(name='yo')
async def yo(ctx):
	await ctx.send(f'yo {ctx.user}')

bot.run(TOKEN)
