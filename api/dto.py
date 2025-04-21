from typing import Optional, List

import strawberry

@strawberry.type
class PokemonAttributeType:
    id: int
    name: str

@strawberry.type
class PokemonType:
    id: int
    name: str
    hp: int
    generation: int
    legendary: bool
    types: List[PokemonAttributeType]


@strawberry.type
class PageMeta:
    next_page: Optional[str] = strawberry.field(description="The next page")

@strawberry.type
class PokemonResponse:
    pokemons: List[PokemonType] = strawberry.field(description="The list of pokemons")
    pagination: PageMeta = strawberry.field(description="Metadata for pagination")

@strawberry.type
class PokemonAttributeResponse:
    attributes: List[PokemonAttributeType] = strawberry.field(description="The list of pokemons types")
    pagination: PageMeta = strawberry.field(description="Metadata for pagination")