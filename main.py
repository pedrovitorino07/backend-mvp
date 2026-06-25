from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

from routes.players_route import player_bp
from routes.franchise_route import franchise_bp
from routes.draft_route import draft_bp
from routes.lottery_route import lottery_bp


app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=False
)

app.register_blueprint(player_bp)
app.register_blueprint(franchise_bp)
app.register_blueprint(lottery_bp)
app.register_blueprint(draft_bp)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "NBA Draft API",
        "description": """
        API para gerenciamento de prospects e simulação do Draft da NBA.

        Funcionalidades:
        - Consulta de franquias
        - Consulta de prospects
        - Cadastro de prospects
        - Remoção de prospects
        - Simulação da Lottery
        - Simulação do Draft
        """,
        "version": "1.0.0"
    }
}

Swagger(app, template=swagger_template)


@app.route("/")
def boas_vindas():
    return "<p>Bem vindo!</p>"


if __name__ == "__main__":
    app.run(debug=True)
