from sqlalchemy import create_engine, Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, relationship
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

pokemon_pokemonAttribute_association = Table(
    'Pokemon_pokemonAttribute',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey("Pokemon.id")),
    Column('pokemon_attribute_id', Integer, ForeignKey("PokemonAttribute.id"))
)

class Pokemon(Base):

    __tablename__ = "Pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean)
    types = relationship('PokemonAttribute', secondary=pokemon_pokemonAttribute_association, back_populates='pokemons')


class PokemonAttribute(Base):
    __tablename__ = "PokemonAttribute"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pokemons = relationship('Pokemon', secondary=pokemon_pokemonAttribute_association, back_populates='types')