from api.repository import  PokemonRepository
from typing import Optional, List
from api.models import Pokemon
from api.dto import *

class PokemonService():

    def __init__(self, pokemon_repository: PokemonRepository):
        self.__pokemon_repository = pokemon_repository

    def __convert_to_graphql_type(self, entity: Pokemon) -> PokemonType:

        return PokemonType(id=entity.id, name=entity.name, hp=entity.hp, generation=entity.generation, legendary=entity.legendary)

    def get_pokemons(self) -> List[PokemonType]:

        pokemons = self.__pokemon_repository.get_pokemons()

        return [self.__convert_to_graphql_type(pokemon) for pokemon in pokemons]

    def get_pokemon_by_id(self, id: int) -> Optional[PokemonType]:
        pokemon = self.__pokemon_repository.get_pokemon_by_id(id)

        if pokemon is None:
            return None

        return self.__convert_to_graphql_type(pokemon)

    def add_pokemon(self, name: str, hp: int, generation: int, legendary: bool) -> PokemonType:

        pokemon = self.__pokemon_repository.add_pokemon(Pokemon(name=name, hp=hp, generation=generation, legendary=legendary))

        return self.__convert_to_graphql_type(pokemon)