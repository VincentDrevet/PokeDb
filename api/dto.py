from typing import Optional, List

import strawberry

@strawberry.type
class PokemonType:
    id: int
    name: str
    hp: int
    generation: int
    legendary: bool


@strawberry.type
class PageMeta:
    next_page: Optional[str] = strawberry.field(description="The next page")

@strawberry.type
class PokemonResponse:
    pokemons: List[PokemonType] = strawberry.field(description="The list of pokemons")
    pagination: PageMeta = strawberry.field(description="Metadata for pagination")