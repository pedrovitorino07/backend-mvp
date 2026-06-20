import random

from models.lotteryResult import LotteryResult


def realizar_lottery(db, franchises):

    db.query(LotteryResult).delete()

    franchises_sorteadas = franchises.copy()

    random.shuffle(franchises_sorteadas)

    resultado = []

    for indice, franchise in enumerate(franchises_sorteadas, start=1):

        lottery = LotteryResult(
            pick=indice,
            franchise_id=franchise.id
        )

        db.add(lottery)

        resultado.append({
            "pick": indice,
            "franchise": franchise.nome
        })

    db.commit()

    return resultado
