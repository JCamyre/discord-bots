import os 
import re 
import sys 
import random
import yfinance as yf

# Import my Stock trading module


from discord.ext import commands
import discord

from dotenv import load_dotenv 


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default() # "Due to an API change Discord is now forcing developers who want member caching to explicitly opt-in to it. This is a Discord mandated change and there is no way to bypass it. In order to get members back you have to explicitly enable the members privileged intent and change the Intents.members attribute to true."
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='yo', help="Sends yo and @'s the user")
async def yo(ctx):
	await ctx.send(f'yo {ctx.user}')

# @bot.command(name='members')
# async def members(ctx):
# 	members = '\n - '.join([member.name for member in guild.members])
# 	await print(f'Guild Members:\n - {members}')
custom_int = lambda x: int(x)

@bot.command(name='dice', help='Rolls a dice with specificied number of sides.')
async def dice(ctx, sides: custom_int):
	await ctx.send('Rolling...')
	await ctx.send(str(random.choice(range(1, sides+1))) + f' <@{ctx.author.id}>')

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='yo'):
	guild = ctx.guild
	existing_channel = discord.utils.get(guild.channels, name=channel_name) # Search through this guild's channels to see if this new channel name already exists
	if not existing_channel:
		print(f'Creating a new channel: {channel_name}')
		await guild.create_text_channel(channel_name)
# yo(ctx, *, args): print(args). !yo testing testing cciv
# $stock cciv

@bot.command(name='stock')
async def stock(ctx, ticker: str):
	ticker = yf.Ticker(ticker)
	try:
		print(ticker.info
	except:
		on_command_error(ctx, 'Ticker does not exist')


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.MissingRequiredArgument):
		await ctx.send(f'You forgot to type something! <@{ctx.author.id}>')


bot.run(TOKEN)
