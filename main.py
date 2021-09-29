import keep_alive
import lmaooo
import discord
import random
#import urllib.request, urllib.parse, urllib.error
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os

client = discord.Client(intents=discord.Intents.all())
#bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
#image = urllib.request.URLopener()
'''
y=input("Enter name of subreddit to download pics:")
numy=int(input("Enter number of pics:"))
numy=numy//5
lmaooo.main(y, numy)'''

'''guildids = [
    436123157850619904, 781405230427406347, 549268455610777600,
    781405230427406347
]'''

def getrandom(f):
    if f == 'hentie':
        file = open('poppy.txt', 'r')
    elif f == 'bleach':
        file = open("bleach.txt", 'r')
    linkylist = eval(file.read())
    print(len(linkylist))
    i = random.randrange(1, len(linkylist) + 1)
    print(i)
    m = linkylist[i - 1]
    m = m.strip('\'')
    return m

guildids=[]
def makeids():
    global guildids
    for guild in client.guilds:
        guildids.append(guild.id)

@slash.slash(name='Hentie',
             description='A command to get nsfw hentie pics',
             guild_ids=guildids)
async def _Hentie(ctx):
    channel_nsfw = ctx.channel.is_nsfw()
    if channel_nsfw:
        nsfw = True
    else:
        nsfw = False
    if nsfw:
        x = getrandom('hentie')
        if 'redgif' or 'gyfcat' or 'i.redd' or 'imgur' in x:
            x = "|| " + x + " ||"
            await ctx.send(x)
        else:
            post = discord.Embed(title="'_'")
            post.set_image(url=x)
            await ctx.send(content='embed', embed=[post])
    else:
        await ctx.send('Only usable in NSFW channels')


@slash.slash(name='Eyebleach',
             description='A command to get a random eyebleach pic',
             guild_ids=guildids)
async def _Eyebleach(ctx):
    x = getrandom('bleach')
    if 'imgur' or 'gyfcat' or 'i.redd' in x:
        await ctx.send(x)
    else:
        post = discord.Embed(title='Best served with bleach')
        post.set_image(url=x)
        await ctx.send(content='eyebleach', embed=[post])


@slash.slash(name='Memestream',
             description='See top 20 memes from today',
             guild_ids=guildids)
async def _Memestream(ctx):
    x = lmaooo.getposts('memes', 20)
    file = open('temp.txt')
    linkylist = eval(file.read())
    for x in linkylist:
        if 'redgif' or 'gyfcat' or 'i.redd' or 'imgur' in x:

            await ctx.send(x)
        else:
            post = discord.Embed(title="'_'")
            post.set_image(url=x)
            await ctx.send(content='meme', embed=[post])


@slash.slash(name='Awwstream',
             description='See top 20 aww images from today',
             guild_ids=guildids)
async def _Awwstream(ctx):
    x = lmaooo.getposts('aww', 20)
    file = open('temp.txt')
    linkylist = eval(file.read())
    for x in linkylist:
        await ctx.send(x)


@slash.slash(name='Bubblewrap',
             description='Bubblewrap in 2021 be like',
             guild_ids=guildids)
async def _Bubblewrap(ctx):
    await ctx.send("||POP|| " * 60)


@slash.slash(name='Hentiestream',
             description='See top 20 hentie from today',
             guild_ids=guildids)
async def _hentiestream(ctx):
    channel_nsfw = ctx.channel.is_nsfw()
    if channel_nsfw:
        nsfw = True
    else:
        nsfw = False
    if nsfw:
        x = lmaooo.getposts('hentai', 20)
        file = open('temp.txt')
        linkylist = eval(file.read())
        for x in linkylist:
            if 'redgif' or 'gyfcat' or 'i.redd' or 'imgur' in x:
                x = "|| " + x + " ||"
                await ctx.send(x)
            else:
                post = discord.Embed(title="'_'")
                post.set_image(url=x)
                await ctx.send(content='hentie', embed=[post])
    else:
        await ctx.send('Only usable in NSFW channels')

@slash.slash(name='Dankmemestream',
             description='See top 20 memes from today',
             guild_ids=guildids)
async def _Dankmemestream(ctx):
    x = lmaooo.getposts('dankmemes', 20)
    file = open('temp.txt')
    linkylist = eval(file.read())
    for x in linkylist:
        if 'redgif' or 'gyfcat' or 'i.redd' or 'imgur' in x:

            await ctx.send(x)
        else:
            post = discord.Embed(title="'_'")
            post.set_image(url=x)
            await ctx.send(content='dankmeme', embed=[post])


@client.event
async def on_ready():
    print(('We have logged in as {0.user}'.format(client)))
    return await client.change_presence(
        activity=discord.Activity(type=3, name='Memestream'))




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel_nsfw = message.channel.is_nsfw()
    if channel_nsfw:
        nsfw = True
    else:
        nsfw = False

    if message.content.startswith('pls hentie') or message.content.startswith(
            'Pls hentie'):
        if nsfw:
            x = getrandom('hentie')
            print(x)
            if 'redgif' or 'gyfcat' or 'i.redd' or 'imgur' in x:
                x = "|| " + x + " ||"
                await message.channel.send(x)
            else:
                post = discord.Embed(title="'_'")
                post.set_image(url=x)
                await message.channel.send(embed=post)
            #await bot.send_message(ctx.message.channel, embed = embed)
        else:
            await message.channel.send('Only usable in NSFW channels')

    if message.content.startswith(
            'pls eyebleach') or message.content.startswith('Pls eyebleach'):
        titl = 'Best served with bleach'
        x = getrandom('bleach')
        if 'imgur' or 'gyfcat' or 'i.redd' in x:
            await message.channel.send(x)
        else:
            post = discord.Embed(title=titl)
            post.set_image(url=x)
            await message.channel.send(embed=post)

    if message.content.startswith(
            'pls memestream') or message.content.startswith('Pls memestream'):
        x = lmaooo.getposts('dankmemes', 20)
        file = open('temp.txt')
        linkylist = eval(file.read())
        for x in linkylist:
            await message.channel.send(x)

    if message.content.startswith(
            'pls dankmemestream') or message.content.startswith(
                'Pls dankmemestream'):
        x = lmaooo.getposts('dankmemes', 20)
        file = open('temp.txt')
        linkylist = eval(file.read())
        for x in linkylist:
            await message.channel.send(x)


@client.event
async def on_guild_join(guild):
    makeids()

my_secret = os.environ['TOKEN']
keep_alive.keep_alive()
client.run(my_secret)
