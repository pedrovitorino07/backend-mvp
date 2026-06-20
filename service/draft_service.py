def realizar_draft(franchises, players):

    resultado = []

    for indice, (franchise, player) in enumerate(
        zip(franchises, players),
        start=1
    ):

        resultado.append({
            "pick": indice,
            "franchise": franchise.nome,
            "player": player.nome,
            "posicao": player.posicao
        })

    return resultado
