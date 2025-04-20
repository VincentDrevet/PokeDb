from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os


engine = create_engine(f"sqlite:///{os.getcwd()}/pokemon.db")

db_session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)

Base = declarative_base()

class Pokemon(Base):

    __tablename__ = "Pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean)
