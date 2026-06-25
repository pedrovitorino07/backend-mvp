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

    lottery_results = (
        db.query(LotteryResult)
        .order_by(LotteryResult.pick)
        .all()
    )

    if not lottery_results:
        db.close()
        return {
            "erro": "Execute a lottery antes do draft"
        }, 400

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

    players = (
        db.query(Player)
        .order_by(Player.ranking)
        .all()
    )

    resultado = realizar_draft(
        franchises,
        players
    )

    db.close()

    return resultado
