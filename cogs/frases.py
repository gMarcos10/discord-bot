import discord
from discord.ext import commands
from discord import app_commands

class Frases(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(
        name="frase", 
        description="Envia uma frase para o canal #frasesinhas"
    )
    #O describe olha para a função que está logo abaixo dele.
    @app_commands.describe(
    usuario="Escolha um usuário",
    frase="Digite a frase"
    )

    async def frase(
        self,
        interaction: discord.Interaction, #interaction é tipo o context mas para slash commands
        frase: str,
        usuario: discord.Member
    ):
        
        #Pegar o canal com o nome "frasesinhas"
        canal = discord.utils.get(
            interaction.guild.text_channels,
            name="frasesinhas"
        )

        if canal is None:
            await interaction.response.send_message(
                "Cadê a porra do canal #frasesinhas?",
                ephemeral=True
                )
            return

        await canal.send(f'*"{frase}"* {usuario.mention}')

        await interaction.response.send_message(
        "Frase registrada no canal #frasesinhas!",
        ephemeral=True #ephemeral true significa que só quem mandou o comando que ve essa mensagem de confirmação
        )
async def setup(bot):
    await bot.add_cog(Frases(bot))