from discord.ext import commands
from comic_trick import ComicTrick
from comic_hunger import ComicHungerLevel
from comic_bar import ComicBarLevel
import discord

CHANNEL_ID = 1148349444996214874
BOT_TOKEN = "BOT TOKEN"


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("...comic side eyes you with a disappointed look and does not woof a word...")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Comic is hungry *side eyes you*")

@bot.command()
async def hello(ctx):
    await ctx.send("*side eye*")

@bot.command()
async def treat(ctx, x):
    tricklevel = ComicTrick()
    result = tricklevel.do_trick(x)
    await ctx.send(result)

@bot.command()
async def feed(ctx, x):
    hungrylevel = ComicHungerLevel()
    result = hungrylevel.feed_food(x)
    await ctx.send(result)

@bot.command()
async def checkbar(ctx):
    barcheck = ComicBarLevel()
    print(f"result: {barcheck.__getbar__()}")
    result = f"Comic's current satisfaction level: {barcheck.__getbar__()}"
    await ctx.send(result)

bot.run(BOT_TOKEN)
