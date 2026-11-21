import discord
from discord.ext import commands
from discord import app_commands #aqui é onde fica os slash commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all() #guardando todas as permissões na variável
bot = commands.Bot(".", intents=intents) #cria o bot

async def main():
    async with bot: #enquanto o bot estiver funcionando
        await bot.load_extension("cogs.geral")
        await bot.load_extension("cogs.diversao")
        await bot.load_extension("cogs.frases")
        await bot.load_extension("cogs.eventos")
        await bot.load_extension("cogs.moderacao")
        await bot.load_extension("cogs.bingo")

        await bot.start(TOKEN)

asyncio.run(main())