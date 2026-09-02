import discord
import random
from discord.ext import commands
from discord import app_commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

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
                await interaction.response.send_message(f"Bing **{titulo}** iniciado.\nDigite /palpite para dar o seu palpite.")
                return
            await interaction.response.send_message(f"Bingo **{titulo}** iniciado.\nDigite /palpite para dar o seu palpite.")

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
        for palpite_id, palpite in enumerate(self.palpites, start=1):
            lista += f"{palpite_id}. {palpite.texto}\n"

        embed_palpites = discord.Embed(
            title=f"Palpites para {self.titulo}   {len(self.palpites)}/{self.tamanho}",
            description=lista
        )

        await interaction.response.send_message(embed=embed_palpites)

    @app_commands.command(name="removerpalpite", description="Remova um palpite digitando o Id")
    @app_commands.describe(palpite_id = "Digite o Id do palpite (número que aparece na lista de palpites)")
    #Id será a posição na lista
    async def removerpalpite(self, interaction: discord.Interaction, palpite_id:int):
        if palpite_id < 1 or palpite_id > len(self.palpites):
            await interaction.response.send_message(
                "Esse ID de palpite não existe.",
                ephemeral=True
            )
            return
        indice = palpite_id - 1 # a lista começa a contar do 0, então precisa subtrair 1
        palpite = self.palpites[indice]
        if palpite.autor_id != interaction.user.id:
            await interaction.response.send_message("Esse palpite não é seu.", ephemeral=True)
        else:
            self.palpites.pop(indice)
            await interaction.response.send_message("Palpite removido com sucesso!", ephemeral=True)

# ===================================================================================================

    def criar_imagem_cartela(self):

        # Tamanho da cartela
        tamanho = 5 if self.tamanho == 24 else 4

        # Dimensões da imagem
        largura = 1000
        altura = 1000

        # Tamanho de cada quadrado
        tamanho_quadrado = largura // tamanho

        # Cria a imagem
        imagem = Image.new("RGB", (largura, altura), "white")
        desenho = ImageDraw.Draw(imagem)

        # Fonte
        fonte_letra = ImageFont.truetype("arial.ttf", 50)
        fonte_palpite = ImageFont.truetype("arial.ttf", 25)

        # Desenha os quadrados
        for linha in range(tamanho):
            for coluna in range(tamanho):

                x1 = coluna * tamanho_quadrado
                y1 = linha * tamanho_quadrado

                x2 = x1 + tamanho_quadrado
                y2 = y1 + tamanho_quadrado

                desenho.rectangle(
                    (x1, y1, x2, y2),
                    outline="black",
                    width=3
                )

        # Coloca os palpites
        indice_palpite = 0

        for linha in range(tamanho):
            for coluna in range(tamanho):

                # FREE no centro do bingo 5x5
                if tamanho == 5 and linha == 2 and coluna == 2:
                    texto = "FREE"

                else:
                    palpite = self.palpites[indice_palpite]
                    texto = palpite.texto

                    indice_palpite += 1

                x = coluna * tamanho_quadrado + tamanho_quadrado // 2
                y = linha * tamanho_quadrado + tamanho_quadrado // 2

                desenho.text(
                    (x, y),
                    texto,
                    font=fonte_palpite,
                    fill="black",
                    anchor="mm"
                )

        # Salva a imagem na memória
        arquivo = BytesIO()
        imagem.save(arquivo, format="PNG")
        arquivo.seek(0)

        return arquivo
    
# ===================================================================================================
    
    @app_commands.command(name="gerarcartela", description="Embaralha os palpites e gera a cartela do bingo")
    async def gerarcartela(self, interaction: discord.Interaction):
        if len(self.palpites) != self.tamanho:
            await interaction.response.send_message("A cartela ainda não está cheia.")
            return
        random.shuffle(self.palpites)

        imagem = self.criar_imagem_cartela()

        arquivo = discord.File(
            imagem,
            filename="cartela.png"
        )

        embed = discord.Embed(
            title=f"Bingo: {self.titulo}"
        )

        embed.set_image(url="attachment://cartela.png")

        await interaction.response.send_message(
            embed=embed,
            file=arquivo
        )

async def setup(bot):
    await bot.add_cog(Bingo(bot))