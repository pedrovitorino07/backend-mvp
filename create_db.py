from database import Base, engine

from models.players import Player
from models.franchises import Franchise
from models.lotteryResult import LotteryResult

Base.metadata.create_all(bind=engine)

print("Banco criado!")
