import datetime

from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_globals import engine

Base = declarative_base()


class GDP(Base):
    __tablename__ = 'gdp'
    country = Column(String, primary_key = True)
    year = Column(Integer, primary_key = True)
    gdp = Column(Float)
    timestamp = Column(DateTime, default = datetime.datetime.utcnow)


class HistoricalGDP(Base):
    __tablename__ = 'historical_gdp'
    region = Column(String, primary_key = True)
    year = Column(Integer, primary_key = True)
    gdp = Column(Float)
    percent = Column(Float)
    timestamp = Column(DateTime, default = datetime.datetime.utcnow)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# recreate_database()