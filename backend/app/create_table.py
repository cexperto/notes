from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from config import host, port, database, user, password


Base = declarative_base()


conn_str = f'postgresql://{user}:{password}@{host}/{database}'
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()
