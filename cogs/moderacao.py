import discord
from discord.ext import commands

class Moderacao(commands.Cog):

    def __init__(self, bot): #construtor
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True) #só quem tem permissão de administrar mensagens
    async def limpar(self, ctx:commands.Context, num_mensagens:int):
        if num_mensagens < 1:
            await ctx.send("Informe uma quantidade maior que 0.")
            return
        await ctx.channel.purge(limit=num_mensagens+1)

async def setup(bot):
    await bot.add_cog(Moderacao(bot))      