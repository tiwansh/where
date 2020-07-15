from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:pass1234@localhost/where')
connection = engine.connect()
Session = sessionmaker(bind = engine)
postgres_session = Session()
