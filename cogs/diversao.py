from discord.ext import commands
import random
import asyncio

class Diversao(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dado(self, ctx:commands.Context, faces:int):
        if faces < 2:
            await ctx.send("Um dado precisa de pelo menos 2 lados")
            return
        await ctx.send(f'🎲 Girando um dado com **{faces}** lados...')

        await asyncio.sleep(1.5)
        numero_dado = random.randint(1,faces)
        await ctx.send(f'🎉 Caiu o número **{numero_dado}**!')

async def setup(bot):
    await bot.add_cog(Diversao(bot))