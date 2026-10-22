import discord
from discord.ext import commands
from discord import app_commands

class Geral(commands.Cog):

    def __init__(self, bot): #construtor
        self.bot = bot

    @commands.command()
    async def oi(self, ctx:commands.Context): #Tipar o context faz o python saber q é do tipo commands.
        await ctx.reply(f"Olá, {ctx.author.name}!") #reply não só manda msg, ele responde a mensagem do .oi

    @commands.command()
    async def falar(self, ctx:commands.Context, *, texto):
        await ctx.send(texto)

    @app_commands.command(
        name="avatar", 
        description="Exibe a foto de perfil de algum usuário"
    )
    #O describe olha para a função que está logo abaixo dele.
    @app_commands.describe(usuario="Escolha um usuário")
    async def avatar(
        self,
        interaction: discord.Interaction, #interaction é tipo o context mas para slash commands
        usuario: discord.Member
    ):
        avatar_embed = discord.Embed(title=f"Foto de perfil de {usuario.name}")
        avatar_embed.set_image(url=usuario.display_avatar.url)
        await interaction.response.send_message(embed=avatar_embed)

    @app_commands.command(
        name="help",
        description="Exibe uma lista com todos os comandos disponíveis"
    )
    async def help(
        self,
        interaction: discord.Interaction
    ):
        lista_comandos = []
        comandos = self.bot.tree.get_commands()
        for comando in comandos:
            lista_comandos.append((comando.name, comando.description))

        lista_comandos_embed = discord.Embed(title="Lista de comandos")
        for nome, descricao in lista_comandos:
            lista_comandos_embed.add_field(
                name=nome,
                value=descricao,
                inline=False
            )

        await interaction.response.send_message(embed=lista_comandos_embed)

async def setup(bot):
    await bot.add_cog(Geral(bot))