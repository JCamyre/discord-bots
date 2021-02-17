# @bot.event
# async def on_ready():
# 	guild = discord.utils.get(bot.guilds, name=GUILD) # bot.guilds[0] == GUILD

# 	print(
# 		f'{bot.user} has connected to Discord!\n'
# 		f'{guild.name}(id: {guild.id})'
# 	)

# 	members = '\n - '.join([member.name for member in guild.members])
# 	print(f'Guild Members:\n - {members}')

# @bot.event
# async def on_member_join(member):
# 	await member.create_dm()
# 	await member.dm_channel.send( # send a message in the member's dm
# 		f'yo {member.name}'
# 	)

# 	members = '\n - '.join([member.name for member in guild.members])
# 	print(f'Guild Members:\n - {members}')


# @bot.event
# async def on_message(message):
# 	if message.author == bot.user:
# 		return 

	# yo
	# yo = re.compile(r'\byo\b')

	# if yo.search(message.content): 
	# 	await message.channel.send('yo') # In that message's channel, send response


# @bot.event
# async def on_error(event, *args, **kwargs):
# 	with open('err.log', 'a') as f: # append to file
# 		if event == 'on_message':
# 			f.write(f'Unhandled message: {args[0]}. Error: {sys.exc_info()}\n')
# 		else:
# 			raise # If any other error besides on_message, raise the error so we see it in the console