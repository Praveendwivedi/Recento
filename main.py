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
user = api.get_user('Praveen')
print(user.screen_name)
print(user.followers_count)

# public_tweets = api.home_timeline()
# print('5')
# for tweet in public_tweets:
#     print(tweet.text).encode(encoding='UTF-8',errors='ignore')
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
  if 'inspire' in msg.content.lower():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await msg.channel.send(quote)
  
  
  
client.run(os.getenv('TOKEN'))
