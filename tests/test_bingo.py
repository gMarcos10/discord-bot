from cogs.bingo import Palpite

def test_palpite_guarda_texto_e_autor():
    palpite = Palpite("Minecraft", 123456)

    assert palpite.texto == "Minecraft"
    assert palpite.autor_id == 123456