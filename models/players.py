from sqlalchemy import Column, Integer, String, Float
from database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer)
    posicao = Column(String)
    universidade = Column(String)
    altura = Column(Float)
    nacionalidade = Column(String)
    ranking = Column(Integer)
