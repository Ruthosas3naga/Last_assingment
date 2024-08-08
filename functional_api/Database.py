from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "sqlite:///./portfolio.db" #data base credential

#NB - Only when using sqlite, do we make use of connect_args
engine = create_engine(DB_URL,connect_args={"check_same_thread":False})

#This means the session maker is going to work with "engine" 
db_session = sessionmaker(bind=engine, autocommit=False, autoflush=False) #interact with database

#provides us with tools to create tables in our database
Base = declarative_base() 