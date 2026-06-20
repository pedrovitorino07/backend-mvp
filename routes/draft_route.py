from flask import Blueprint

from database import SessionLocal
from models.franchises import Franchise
from models.players import Player
from models.lotteryResult import LotteryResult

from service.draft_service import realizar_draft

draft_bp = Blueprint("draft", __name__)


@draft_bp.route("/draft", methods=["POST"])
def draft():
    """
    Executa um draft completo
    ---
    tags:
      - Draft

    responses:
      200:
        description: Resultado do draft
    """

    db = SessionLocal()

    # Busca a ordem salva pela lottery
    lottery_results = (
        db.query(LotteryResult)
        .order_by(LotteryResult.pick)
        .all()
    )

    # Impede executar draft sem lottery
    if not lottery_results:
        db.close()
        return {
            "erro": "Execute a lottery antes do draft"
        }, 400

    # Monta a lista de franquias na ordem sorteada
    franchises = []

    for lottery in lottery_results:

        franchise = (
            db.query(Franchise)
            .filter(
                Franchise.id == lottery.franchise_id
            )
            .first()
        )

        franchises.append(franchise)

    # Busca os jogadores ordenados pelo ranking
    players = (
        db.query(Player)
        .order_by(Player.ranking)
        .all()
    )

    # Executa o draft
    resultado = realizar_draft(
        franchises,
        players
    )

    db.close()

    return resultado
