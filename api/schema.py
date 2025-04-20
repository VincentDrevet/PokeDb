import asyncio

import strawberry
from typing import List, Annotated, Optional, AsyncGenerator
from api.services import  PokemonService
from api.repository import PokemonRepository
from strawberry.field_extensions import InputMutationExtension
from api.models import Pokemon
from strawberry import Schema
from api.models import db_session
from api.dto import *



pokemon_service: PokemonService = PokemonService(PokemonRepository())


@strawberry.type
class Query:

    pokemons: PokemonResponse = strawberry.field(resolver=pokemon_service.get_pokemons_with_pagination)
    pokemon_by_id: Optional[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemon_by_id)
    pokemons_by_name: List[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemon_by_name)



@strawberry.type
class Mutation:
    add_pokemon: PokemonType = strawberry.mutation(extensions=[InputMutationExtension()], resolver=pokemon_service.add_pokemon)

schema = Schema(query=Query, mutation=Mutation)