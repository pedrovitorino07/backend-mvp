from flask import Blueprint, request
from database import SessionLocal
from models.players import Player

player_bp = Blueprint("players", __name__)


@player_bp.route("/players", methods=["GET"])
def get_players():
    """
    Lista todas os jogadores
    ---
    tags:
      - Players
    responses:
      200:
        description: Lista de jogadores
    """

    db = SessionLocal()

    players = db.query(Player).all()

    resultado = []

    for player in players:
        resultado.append({
            "id": player.id,
            "nome": player.nome,
            "idade": player.idade,
            "altura": player.altura,
            "posicao": player.posicao,
            "universidade": player.universidade,
            "nacionalidade": player.nacionalidade
        })

    db.close()

    return resultado


@player_bp.route("/players/<int:id>", methods=["GET"])
def get_player_by_id(id):
    """
    Busca um jogador pelo ID
    ---
    tags:
      - Players

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do jogador

    responses:
      200:
        description: Jogador encontrado

      404:
        description: Jogador não encontrado
    """

    db = SessionLocal()

    player = db.query(Player).filter(Player.id == id).first()

    db.close()

    if not player:
        return {"erro": "Jogador não encontrado"}, 404

    return {
        "id": player.id,
        "nome": player.nome,
        "idade": player.idade,
        "posicao": player.posicao
    }


@player_bp.route("/players", methods=["POST"])
def create_player():
    """
    Cadastra um novo jogador
    ---
    tags:
      - Players

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: Cooper Flagg

            idade:
              type: integer
              example: 18

            posicao:
              type: string
              example: SF

            universidade:
              type: string
              example: Duke

            altura:
              type: number
              example: 2.06

    responses:
      201:
        description: Jogador criado com sucesso

      400:
        description: Dados inválidos
    """

    data = request.get_json()

    db = SessionLocal()

    player = Player(
        nome=data["nome"],
        idade=data["idade"],
        posicao=data["posicao"],
        universidade=data["universidade"],
        altura=data["altura"]
    )

    db.add(player)

    db.commit()

    db.refresh(player)

    db.close()

    return {
        "message": "Jogador criado com sucesso",
        "id": player.id
    }, 201


@player_bp.route("/players/<int:id>", methods=["DELETE"])
def delete_player(id):
    """
    Remove um jogador da lista de prospects
    ---
    tags:
      - Players

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do jogador

    responses:
      200:
        description: Jogador removido com sucesso

      404:
        description: Jogador não encontrado
    """

    db = SessionLocal()

    player = db.query(Player).filter(
        Player.id == id
    ).first()

    if not player:
        db.close()
        return {"error": "Jogador não encontrado"}, 404

    db.delete(player)

    db.commit()

    db.close()

    return {
        "message": f"Jogador {id} removido com sucesso"
    }
