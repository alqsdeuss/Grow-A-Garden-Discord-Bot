import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()
----------------------------------------
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=',', intents=intents)
api = 'https://growagardenapi.vercel.app/api/stock/GetStock'
----------------------------------------
def make_text(items):
    if not items:
        return "api down"
    text = ""
    for item in items:
        emoji = item.get('emoji', '')
        name = item.get('name', 'no name')
        val = item.get('value', '?')
        text += f"{emoji} {name} — {val}\n"
    return text
----------------------------------------
@bot.event
async def ready():
    print(f"username {bot.user}")
----------------------------------------
@bot.command(name='stock')
async def seedsstock(ctx):
    try:
        r = requests.get(api)
        stuff = r.json()
        seeds = stuff.get('seedsStock', [])
        txt = make_text(seeds)
        embed = discord.Embed(description=txt)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("api is down or smt went wrong try again later")
----------------------------------------
@bot.command(name='eggs')
async def eggsstock(ctx):
    try:
        r = requests.get(api)
        stuff = r.json()
        eggs = stuff.get('eggStock', [])
        txt = make_text(eggs)
        embed = discord.Embed(description=txt)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("api is down or smt went wrong try again later")
----------------------------------------
@bot.command(name='event')
async def honeystock(ctx):
    try:
        r = requests.get(api)
        stuff = r.json()
        honey = stuff.get('honeyStock', [])
        txt = make_text(honey)
        embed = discord.Embed(description=txt)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("api is down or smt went wrong try again later")
----------------------------------------
@bot.command(name='cosmetic')
async def cosmeticsstock(ctx):
    try:
        r = requests.get(api)
        stuff = r.json()
        cosmetics = stuff.get('cosmeticsStock', [])
        txt = make_text(cosmetics)
        embed = discord.Embed(description=txt)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("api is down or smt went wrong try again later")
----------------------------------------
@bot.command(name='gear')
async def gearstock(ctx):
    try:
        r = requests.get(api)
        stuff = r.json()
        gear = stuff.get('gearStock', [])
        txt = make_text(gear)
        embed = discord.Embed(description=txt)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("api is down or smt went wrong try again later")
----------------------------------------
bot.run(os.getenv('token'))
