from api.repository import PokemonRepository, PokemonAttributeRepository
from typing import Optional, List
from api.models import Pokemon, PokemonAttribute
from api.dto import *
from api.utils import *

class PokemonService():

    def __init__(self, pokemon_repository: PokemonRepository):
        self.__pokemon_repository = pokemon_repository

    def __convert_to_graphql_type(self, entity: Pokemon) -> PokemonType:

        return PokemonType(id=entity.id, name=entity.name, hp=entity.hp, generation=entity.generation, legendary=entity.legendary)

    #def get_pokemons(self) -> List[PokemonType]:

    #    pokemons = self.__pokemon_repository.get_pokemons()

    #    return [self.__convert_to_graphql_type(pokemon) for pokemon in pokemons]

    def get_pokemon_by_id(self, id: int) -> Optional[PokemonType]:
        pokemon = self.__pokemon_repository.get_pokemon_by_id(id)

        if pokemon is None:
            return None

        return self.__convert_to_graphql_type(pokemon)

    def get_pokemon_by_name(self, pattern: str) -> List[PokemonType]:

        pokemons = self.__pokemon_repository.get_pokemon_by_name(pattern)

        return [self.__convert_to_graphql_type(pokemon) for pokemon in pokemons]

    def get_pokemons_with_pagination(self, page_size: int, cursor: Optional[str] = None) -> PokemonResponse:

        pokemon_id: int = 0

        if cursor is not None:
            pokemon_id = decode_cursor(cursor)

        pokemons = self.__pokemon_repository.get_pokemons_with_pagination(pokemon_id)

        pokemons = pokemons[: page_size + 1]

        # If number of pokemon in list is upper than the limit, it means that they are another page after
        if len(pokemons) > page_size:

            last_pokemon = pokemons.pop(-1)
            cursor = encode_cursor(last_pokemon.id)

            return PokemonResponse(pokemons=pokemons, pagination=PageMeta(next_page=cursor))

        # If number of pokemons in list is lesser or equal to the limit, it means that they are no more pages.

        return PokemonResponse(pokemons=pokemons, pagination=PageMeta(next_page=None))

    def add_pokemon(self, name: str, hp: int, generation: int, legendary: bool) -> PokemonType:

        pokemon = self.__pokemon_repository.add_pokemon(Pokemon(name=name, hp=hp, generation=generation, legendary=legendary))

        return self.__convert_to_graphql_type(pokemon)



class PokemonAttributeService():

    def __convert_to_graphql_type(self, entity: PokemonAttribute) -> PokemonAttributeType:

        return PokemonAttributeType(id=entity.id, name=entity.name)

    def __init__(self, pokemon_attribute_repository: PokemonAttributeRepository):
        self.__pokemon_attribute_repository = pokemon_attribute_repository


    def add_pokemon_attribute(self, name: str) -> PokemonAttributeType:

        pokemon_attribute = self.__pokemon_attribute_repository.add_pokemon_attribute(PokemonAttribute(name=name))

        return self.__convert_to_graphql_type(pokemon_attribute)

    def get_pokemon_attribute_with_pagination(self, page_size: int, cursor: str = None) -> PokemonAttributeResponse:

        pokemon_attribute_id = 0

        if cursor is not None:
            pokemon_attribute_id = decode_cursor(cursor)

        attributes = self.__pokemon_attribute_repository.get_pokemon_attribute(pokemon_attribute_id)

        attributes = attributes[: page_size + 1]

        if len(attributes) > page_size:

            last_attributes = attributes.pop(-1)
            cursor = encode_cursor(last_attributes.id)

            return PokemonAttributeResponse(attributes=attributes, pagination=PageMeta(next_page=cursor))

        return PokemonAttributeResponse(attributes=attributes, pagination=PageMeta(next_page=None))


