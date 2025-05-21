import discord
from discord.ext import commands
from botsifre import sifreolustur

intents = discord.Intents.default()
intents.message_content = True
intents.members=True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):

    for i in range(times):
        await ctx.send(content)

bot.run("token girin")
