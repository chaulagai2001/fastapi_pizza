from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:root@localhost/pizza_deliver',
                       echo = True)

Base = declarative_base()

Session = sessionmaker(bind = engine)
session = Session()