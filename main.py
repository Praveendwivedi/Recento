import discord

client = discord.Client()

@client.event
async def on_ready():
  print('hello, I\'m {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if msg:
    await msg.channel.send('hey')
  
  
client.run(os.getenv('TOKEN'))

