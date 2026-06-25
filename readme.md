# NBA Draft API

API desenvolvida com **Flask**, **SQLAlchemy** e **SQLite** para simular o processo completo do **NBA Draft**, incluindo prospects, franquias e Lottery.

O projeto tem foco acadêmico e simula o comportamento de um draft real de forma simplificada e didática.

---

## Funcionalidades

### Prospects (Jogadores)

- Listar prospects
- Buscar prospect por ID
- Cadastrar prospect
- Remover prospect

### Franquias

- Listar franquias
- Buscar franquia por ID

### Lottery

- Simulação da Lottery para definição da ordem do draft
- Persistência da ordem das picks

### Draft

- Simulação completa do draft da NBA
- Escolha de jogadores por pick
- Resultado final estruturado por franquia e jogador

---

## Tecnologias

- Python 3
- Flask
- Flask-CORS
- SQLAlchemy
- SQLite
- Flasgger (Swagger UI)

## Executando

pip install -r requirements.txt

python create_db.py

python seed.py

python main.py
