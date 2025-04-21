import strawberry
from typing import List, Annotated, Optional, AsyncGenerator
from api.services import  PokemonService, PokemonAttributeService
from api.repository import PokemonRepository, PokemonAttributeRepository
from strawberry.field_extensions import InputMutationExtension
from strawberry import Schema
from api.dto import *



pokemon_service: PokemonService = PokemonService(PokemonRepository())
pokemon_attribute_service: PokemonAttributeService = PokemonAttributeService(PokemonAttributeRepository())

@strawberry.type
class Query:

    pokemons: PokemonResponse = strawberry.field(resolver=pokemon_service.get_pokemons_with_pagination)
    pokemon_by_id: Optional[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemon_by_id)
    pokemons_by_name: List[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemon_by_name)

    pokemon_attributes: PokemonAttributeResponse = strawberry.field(resolver=pokemon_attribute_service.get_pokemon_attribute_with_pagination)



@strawberry.type
class Mutation:
    add_pokemon: PokemonType = strawberry.mutation(extensions=[InputMutationExtension()], resolver=pokemon_service.add_pokemon)
    add_pokemon_attribute: PokemonAttributeType = strawberry.mutation(extensions=[InputMutationExtension()], resolver=pokemon_attribute_service.add_pokemon_attribute)

schema = Schema(query=Query, mutation=Mutation)