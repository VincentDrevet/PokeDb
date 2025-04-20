import strawberry
from typing import List, Annotated, Optional
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

    pokemons: List[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemons)
    pokemon_by_id: Optional[PokemonType] = strawberry.field(resolver=pokemon_service.get_pokemon_by_id)


@strawberry.type
class Mutation:
    add_pokemon: PokemonType = strawberry.mutation(extensions=[InputMutationExtension()], resolver=pokemon_service.add_pokemon)

schema = Schema(query=Query, mutation=Mutation)