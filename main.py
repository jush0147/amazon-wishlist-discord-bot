import discord
import os
from crawler import crawler
from discord.ext import commands, tasks
from keep_alive import keep_alive


id = "輸入你需要的id"

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

TOKEN = os.environ['TOKEN']
CHANNEL_ANNOUNCE = os.environ['CHANNEL_ANNOUNCE']
CHANNEL_LOG = os.environ['CHANNEL_LOG']

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  wishlist.start()
  print("wishlist bot strat")

  


@client.command()
async def hello(ctx):
  print('hello')
  await ctx.send('hello')

@tasks.loop(seconds=600)
async def wishlist():
  
  channel_announce = client.get_channel(int(CHANNEL_ANNOUNCE))
  channel_log = client.get_channel(int(CHANNEL_LOG))
  list = crawler()
  
  if len(list):
    for gift in list:

      embed = discord.Embed(title="Wishlist",           url="https://www.amazon.co.jp/hz/wishlist/ls/1RIS8BD1SC94Y?ref_=wl_share=" + id, description= id + " add " + gift, color=0xef9000)
      embed.set_thumbnail(url="https://i.imgur.com/rcH6WQs.png")
      
      await channel_announce.send(embed=embed)

  print('running')
  
  try:
    await channel_log.send('running')
  except:
    os.system("kill 1")


try:
    keep_alive()
    client.run(TOKEN)
except:
    os.system("kill 1")