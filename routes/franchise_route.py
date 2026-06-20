from flask import Blueprint
from database import SessionLocal
from models.franchises import Franchise

franchise_bp = Blueprint("franchises", __name__)


@franchise_bp.route("/franchises", methods=["GET"])
def get_franchises():
    """
    Lista todas as franquias
    ---
    tags:
      - Franchises
    responses:
      200:
        description: Lista de franquias
    """

    db = SessionLocal()

    franchises = db.query(Franchise).all()

    result = []

    for franchise in franchises:
        result.append({
            "id": franchise.id,
            "nome": franchise.nome,
            "cidade": franchise.cidade,
            "sigla": franchise.sigla,
            "conferencia": franchise.conferencia
        })

    db.close()

    return result


@franchise_bp.route("/franchises/<int:id>", methods=["GET"])
def get_franchise_by_id(id):
    """
    Busca uma franquia pelo ID
    ---
    tags:
      - Franchises

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da franquia

    responses:
      200:
        description: Franquia encontrada

      404:
        description: Franquia não encontrada
    """

    db = SessionLocal()

    franchise = db.query(Franchise).filter(
        Franchise.id == id
    ).first()

    db.close()

    if not franchise:
        return {"erro": "Franquia não encontrada"}, 404

    return {
        "id": franchise.id,
        "nome": franchise.nome,
        "cidade": franchise.cidade,
        "sigla": franchise.sigla,
        "conferencia": franchise.conferencia
    }
