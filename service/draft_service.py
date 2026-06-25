import random


def realizar_draft(franchises, players):

    resultado = []

    jogadores_disponiveis = players.copy()

    for indice, franchise in enumerate(franchises, start=1):

        if not jogadores_disponiveis:
            break

        jogador = random.choice(jogadores_disponiveis)

        jogadores_disponiveis.remove(jogador)

        resultado.append({
            "pick": indice,
            "franchise": franchise.nome,
            "player": jogador.nome,
            "posicao": jogador.posicao
        })

    return resultado
