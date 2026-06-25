import random

from database import SessionLocal
from models.players import Player
from models.franchises import Franchise
from models.lotteryResult import LotteryResult

db = SessionLocal()

players = [
    Player(
        nome="Cooper Flagg",
        idade=18,
        posicao="SF",
        universidade="Duke",
        altura=2.06,
        nacionalidade="EUA",
        ranking=random.randint(1, 100)
    ),
    Player(
        nome="Dylan Harper",
        idade=19,
        posicao="PG",
        universidade="Rutgers",
        altura=1.98,
        nacionalidade="EUA",
        ranking=random.randint(1, 100)
    ),
    Player(
        nome="Ace Bailey",
        idade=18,
        posicao="SF",
        universidade="Rutgers",
        altura=2.03,
        nacionalidade="EUA",
        ranking=random.randint(1, 100)
    ),
    Player(
        nome="VJ Edgecombe",
        idade=19,
        posicao="SG",
        universidade="Baylor",
        altura=1.96,
        nacionalidade="Bahamas",
        ranking=random.randint(1, 100)
    ),
    Player(
        nome="Khaman Maluach",
        idade=18,
        posicao="C",
        universidade="Duke",
        altura=2.18,
        nacionalidade="Sudão do Sul",
        ranking=random.randint(1, 100)
    )
]

franchises = [
    Franchise(nome="Atlanta Hawks", cidade="Atlanta",
              sigla="ATL", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/atl.png"),
    Franchise(nome="Boston Celtics", cidade="Boston",
              sigla="BOS", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/bos.png"),
    Franchise(nome="Brooklyn Nets", cidade="Brooklyn",
              sigla="BKN", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/bkn.png"),
    Franchise(nome="Charlotte Hornets", cidade="Charlotte",
              sigla="CHA", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/cha.png"),
    Franchise(nome="Chicago Bulls", cidade="Chicago",
              sigla="CHI", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/chi.png"),
    Franchise(nome="Cleveland Cavaliers", cidade="Cleveland",
              sigla="CLE", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/cle.png"),
    Franchise(nome="Detroit Pistons", cidade="Detroit",
              sigla="DET", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/det.png"),
    Franchise(nome="Indiana Pacers", cidade="Indiana",
              sigla="IND", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/ind.png"),
    Franchise(nome="Miami Heat", cidade="Miami",
              sigla="MIA", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/mia.png"),
    Franchise(nome="Milwaukee Bucks", cidade="Milwaukee",
              sigla="MIL", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/mil.png"),
    Franchise(nome="New York Knicks", cidade="New York",
              sigla="NYK", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/nyk.png"),
    Franchise(nome="Orlando Magic", cidade="Orlando",
              sigla="ORL", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/orl.png"),
    Franchise(nome="Philadelphia 76ers", cidade="Philadelphia",
              sigla="PHI", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/phi.png"),
    Franchise(nome="Toronto Raptors", cidade="Toronto",
              sigla="TOR", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/tor.png"),
    Franchise(nome="Washington Wizards", cidade="Washington",
              sigla="WAS", conferencia="East", logo="https://a.espncdn.com/i/teamlogos/nba/500/was.png"),

    Franchise(nome="Dallas Mavericks", cidade="Dallas",
              sigla="DAL", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/dal.png"),
    Franchise(nome="Denver Nuggets", cidade="Denver",
              sigla="DEN", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/den.png"),
    Franchise(nome="Golden State Warriors", cidade="San Francisco",
              sigla="GSW", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/gsw.png"),
    Franchise(nome="Houston Rockets", cidade="Houston",
              sigla="HOU", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/hou.png"),
    Franchise(nome="Los Angeles Clippers", cidade="Los Angeles",
              sigla="LAC", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/lac.png"),
    Franchise(nome="Los Angeles Lakers", cidade="Los Angeles",
              sigla="LAL", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/lal.png"),
    Franchise(nome="Memphis Grizzlies", cidade="Memphis",
              sigla="MEM", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/mem.png"),
    Franchise(nome="Minnesota Timberwolves", cidade="Minneapolis",
              sigla="MIN", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/min.png"),
    Franchise(nome="New Orleans Pelicans", cidade="New Orleans",
              sigla="NOP", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/no.png"),
    Franchise(nome="Oklahoma City Thunder", cidade="Oklahoma City",
              sigla="OKC", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/okc.png"),
    Franchise(nome="Phoenix Suns", cidade="Phoenix",
              sigla="PHX", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/phx.png"),
    Franchise(nome="Portland Trail Blazers", cidade="Portland",
              sigla="POR", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/por.png"),
    Franchise(nome="Sacramento Kings", cidade="Sacramento",
              sigla="SAC", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/sac.png"),
    Franchise(nome="San Antonio Spurs", cidade="San Antonio",
              sigla="SAS", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/sas.png"),
    Franchise(nome="Utah Jazz", cidade="Salt Lake City",
              sigla="UTA", conferencia="West", logo="https://a.espncdn.com/i/teamlogos/nba/500/utah.png")
]

db.add_all(players)
db.add_all(franchises)

db.commit()
db.close()
