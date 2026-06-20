from sqlalchemy import Column, Integer, String
from database import Base


class Franchise(Base):
    __tablename__ = "franchises"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    sigla = Column(String, nullable=False)
    conferencia = Column(String, nullable=False)
