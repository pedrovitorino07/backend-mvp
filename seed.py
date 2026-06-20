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
        ranking=1
    ),
    Player(
        nome="Dylan Harper",
        idade=19,
        posicao="PG",
        universidade="Rutgers",
        altura=1.98,
        nacionalidade="EUA",
        ranking=2
    ),
    Player(
        nome="Ace Bailey",
        idade=18,
        posicao="SF",
        universidade="Rutgers",
        altura=2.03,
        nacionalidade="EUA",
        ranking=3
    ),
    Player(
        nome="VJ Edgecombe",
        idade=19,
        posicao="SG",
        universidade="Baylor",
        altura=1.96,
        nacionalidade="Bahamas",
        ranking=4
    ),
    Player(
        nome="Khaman Maluach",
        idade=18,
        posicao="C",
        universidade="Duke",
        altura=2.18,
        nacionalidade="Sudão do Sul",
        ranking=5
    )
]

franchises = [
    Franchise(nome="Atlanta Hawks", cidade="Atlanta",
              sigla="ATL", conferencia="East"),
    Franchise(nome="Boston Celtics", cidade="Boston",
              sigla="BOS", conferencia="East"),
    Franchise(nome="Brooklyn Nets", cidade="Brooklyn",
              sigla="BKN", conferencia="East"),
    Franchise(nome="Charlotte Hornets", cidade="Charlotte",
              sigla="CHA", conferencia="East"),
    Franchise(nome="Chicago Bulls", cidade="Chicago",
              sigla="CHI", conferencia="East"),
    Franchise(nome="Cleveland Cavaliers", cidade="Cleveland",
              sigla="CLE", conferencia="East"),
    Franchise(nome="Detroit Pistons", cidade="Detroit",
              sigla="DET", conferencia="East"),
    Franchise(nome="Indiana Pacers", cidade="Indiana",
              sigla="IND", conferencia="East"),
    Franchise(nome="Miami Heat", cidade="Miami",
              sigla="MIA", conferencia="East"),
    Franchise(nome="Milwaukee Bucks", cidade="Milwaukee",
              sigla="MIL", conferencia="East"),
    Franchise(nome="New York Knicks", cidade="New York",
              sigla="NYK", conferencia="East"),
    Franchise(nome="Orlando Magic", cidade="Orlando",
              sigla="ORL", conferencia="East"),
    Franchise(nome="Philadelphia 76ers", cidade="Philadelphia",
              sigla="PHI", conferencia="East"),
    Franchise(nome="Toronto Raptors", cidade="Toronto",
              sigla="TOR", conferencia="East"),
    Franchise(nome="Washington Wizards", cidade="Washington",
              sigla="WAS", conferencia="East"),

    Franchise(nome="Dallas Mavericks", cidade="Dallas",
              sigla="DAL", conferencia="West"),
    Franchise(nome="Denver Nuggets", cidade="Denver",
              sigla="DEN", conferencia="West"),
    Franchise(nome="Golden State Warriors", cidade="San Francisco",
              sigla="GSW", conferencia="West"),
    Franchise(nome="Houston Rockets", cidade="Houston",
              sigla="HOU", conferencia="West"),
    Franchise(nome="Los Angeles Clippers", cidade="Los Angeles",
              sigla="LAC", conferencia="West"),
    Franchise(nome="Los Angeles Lakers", cidade="Los Angeles",
              sigla="LAL", conferencia="West"),
    Franchise(nome="Memphis Grizzlies", cidade="Memphis",
              sigla="MEM", conferencia="West"),
    Franchise(nome="Minnesota Timberwolves", cidade="Minneapolis",
              sigla="MIN", conferencia="West"),
    Franchise(nome="New Orleans Pelicans", cidade="New Orleans",
              sigla="NOP", conferencia="West"),
    Franchise(nome="Oklahoma City Thunder", cidade="Oklahoma City",
              sigla="OKC", conferencia="West"),
    Franchise(nome="Phoenix Suns", cidade="Phoenix",
              sigla="PHX", conferencia="West"),
    Franchise(nome="Portland Trail Blazers", cidade="Portland",
              sigla="POR", conferencia="West"),
    Franchise(nome="Sacramento Kings", cidade="Sacramento",
              sigla="SAC", conferencia="West"),
    Franchise(nome="San Antonio Spurs", cidade="San Antonio",
              sigla="SAS", conferencia="West"),
    Franchise(nome="Utah Jazz", cidade="Salt Lake City",
              sigla="UTA", conferencia="West")
]

db.add_all(players)
db.add_all(franchises)

db.commit()
db.close()
