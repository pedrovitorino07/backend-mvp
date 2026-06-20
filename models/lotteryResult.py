from sqlalchemy import Column, Integer

from database import Base


class LotteryResult(Base):
    __tablename__ = "lottery_results"

    id = Column(Integer, primary_key=True)
    pick = Column(Integer, nullable=False)
    franchise_id = Column(Integer, nullable=False)
