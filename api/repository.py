from api.models import *
from typing import List, Optional


class PokemonRepository:

    def get_pokemons(self) -> List[Pokemon]:

        return db_session.query(Pokemon).all()

    def get_pokemons_with_pagination(self, id: int) -> List[Pokemon]:

        return db_session.query(Pokemon).filter(Pokemon.id >= id).all()


    def get_pokemon_by_id(self, id: int) -> Optional[Pokemon]:

        return db_session.query(Pokemon).filter(Pokemon.id == id).first()

    def get_pokemon_by_name(self, pattern: str) -> List[Pokemon]:

        return db_session.query(Pokemon).filter(Pokemon.name.startswith(pattern))

    def add_pokemon(self, pokemon: Pokemon):

        try:
            db_session.add(pokemon)
            db_session.commit()
            return pokemon
        except Exception as e:
            raise e

    def count(self) -> int:

        return db_session.query(Pokemon).count()

class PokemonAttributeRepository:

    def add_pokemon_attribute(self, pokemon_attribute: PokemonAttribute):

        try:
            db_session.add(pokemon_attribute)
            db_session.commit()
            return pokemon_attribute
        except Exception as e:
            raise e

    def get_pokemon_attribute(self, index: int) -> List[PokemonAttribute]:

        return db_session.query(PokemonAttribute).filter(PokemonAttribute.id >= index).all()

    def get_pokemon_attribute_by_id(self, id: int) -> Optional[PokemonAttribute]:

        return db_session.query(PokemonAttribute).filter(PokemonAttribute.id == id).first()


    def count(self) -> int:

        return db_session.query(PokemonAttribute).count()