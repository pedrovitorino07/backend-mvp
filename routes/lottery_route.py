from flask import Blueprint

from database import SessionLocal
from models.franchises import Franchise
from service.lottery_service import realizar_lottery

lottery_bp = Blueprint("lottery", __name__)


@lottery_bp.route("/lottery", methods=["POST"])
def lottery():
    """
    Executa a lottery do draft
    ---
    tags:
      - Lottery

    responses:
      200:
        description: Ordem das picks sorteada
    """

    db = SessionLocal()

    franchises = db.query(Franchise).all()

    resultado = realizar_lottery(
        db,
        franchises
    )

    db.close()

    return resultado
