import discord
from discord.ext import commands
from discord import app_commands

class Palpite:
    def __init__(self, texto, autor_id):
        self.texto = texto
        self.autor_id = autor_id

class Bingo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bingo_ativo = False
        self.titulo = ""
        self.tamanho = 0
        self.palpites = []

    async def iniciar_bingo(self, interaction: discord.Interaction, titulo:str, tamanho:int):
            if self.bingo_ativo: #não precisa de colocar == true
                await interaction.response.send_message("Já existe um bingo ativo.")
                return
            self.bingo_ativo = True
            self.titulo = titulo
            self.tamanho = tamanho
            self.palpites = []
            if self.tamanho == 16:
                await interaction.response.send_message(f"Bing **{titulo}** iniciado.\nDigite /palpipi para dar o seu palpipi.")
                return
            await interaction.response.send_message(f"Bingo **{titulo}** iniciado.\nDigite /palpipi para dar o seu palpipi.")

    @app_commands.command(
        name = "criarbingo",
        description = "Inicia uma sessão de bingo"
    )
    @app_commands.describe(
        titulo = "Digite o título do filme"
    )
    async def criarbingo(self, interaction: discord.Interaction, titulo:str):
        await self.iniciar_bingo(
            interaction,
            titulo,
            24
        )

    @app_commands.command(
        name = "criarbing",
        description = "Inicia uma sessão de bing"
    )
    @app_commands.describe(
        titulo = "Digite o título do filme"
    )
    async def criarbing(self, interaction: discord.Interaction, titulo:str):
        await self.iniciar_bingo(
            interaction,
            titulo,
            16
        )

# ===================================================================================================
    
    @app_commands.command(name="palpite", description="Adiciona um palpite ao bingo ativo")
    @app_commands.describe(texto = "Digite algo que você acha que pode acontecer no filme")
    async def add_palpite(self, interaction: discord.Interaction, texto:str):
            novo_palpite = Palpite(texto, interaction.user.id)
            if self.bingo_ativo:
                 if len(self.palpites) < self.tamanho:
                    self.palpites.append(novo_palpite)
                    await interaction.response.send_message(f"Palpipe **{texto}** adicionado! {len(self.palpites)}/{self.tamanho}",
                                                            ephemeral=True)
                 else:
                    await interaction.response.send_message("A cartela já está cheia de palpipes.", ephemeral=True)
            else:
                await interaction.response.send_message("Não há bingo ativo.", ephemeral=True)

    @app_commands.command(name="mostrarpalpites", description="Mostra a lista de palpites do bingo ativo")
    async def mostrar_palpites(self, interaction: discord.Interaction):
        if not self.palpites: #se a lista de palpites estiver vazia
            await interaction.response.send_message("Não há palpipes ainda.")
            return
        
        lista = ""
        for numero, palpite in enumerate(self.palpites, start=1):
            lista += f"{numero}. {palpite.texto}\n"

        embed_palpites = discord.Embed(
            title=f"Palpites para {self.titulo}   {len(self.palpites)}/{self.tamanho}",
            description=lista
        )

        await interaction.response.send_message(embed=embed_palpites)

async def setup(bot):
    await bot.add_cog(Bingo(bot))

    #@app_commands.command(name="removerpalpipi")
    