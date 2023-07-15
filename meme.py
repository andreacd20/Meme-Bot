import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def code(ctx):
    img_name1 = random.choice(os.listdir('codememes'))
    with open(f'codememes/{img_name1}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture1 = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture1)

@bot.command()
async def school(ctx):
    img_name2 = random.choice(os.listdir('schoolmemes'))
    with open(f'schoolmemes/{img_name2}', 'rb') as f:
        picture2 = discord.File(f)
    await ctx.send(file=picture2)

@bot.command()
async def math(ctx):
    img_name3 = random.choice(os.listdir('mathmemes'))
    with open(f'mathmemes/{img_name3}', 'rb') as f:
        picture3 = discord.File(f)
    await ctx.send(file=picture3)
    
bot.run("TOKEN")
