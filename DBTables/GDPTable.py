import datetime

from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:pass1234@localhost/where')
connection = engine.connect()

Base = declarative_base()


class GDP(Base):
    __tablename__ = 'gdp'
    country = Column(String, primary_key = True)
    year = Column(Integer, primary_key = True)
    gdp = Column(Float)
    timestamp = Column(DateTime, default = datetime.datetime.utcnow)


# Base.metadata.create_all(engine)
