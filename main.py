import discord
import os
import requests,json
import tweepy


consumer_key=os.getenv('C_K')
consumer_secret=os.getenv('C_S')
access_token=os.getenv('A_T')
access_token_secret=os.getenv('A_S')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.json())
print(r.status_code)
client = discord.Client()

@client.event
async def on_ready():
  print('hello, I\'m {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if msg:
    print(msg)
    await msg.channel.send('hey {}'.format(msg.author.name))
    tweets = api.search(msg.content,lang='en',result_type='recent',include_entities="mashable")
    for tweet in  tweets:
      if not tweet.text.startswith('RT'):
        await msg.channel.send(tweet.user.screen_name+' : \n'+tweet.text)
  
  
  
  
client.run(os.getenv('TOKEN'))
