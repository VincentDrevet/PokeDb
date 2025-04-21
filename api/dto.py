from typing import Optional, List, Iterable
from strawberry import relay, Info
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
    count: int = strawberry.field(description="Total number of elements")
    next_page: Optional[str] = strawberry.field(description="The next page")

@strawberry.type
class PokemonResponse:
    pokemons: List[PokemonType] = strawberry.field(description="The list of pokemons")
    metadata: PageMeta = strawberry.field(description="Metadata")

@strawberry.type
class PokemonAttributeResponse:
    attributes: List[PokemonAttributeType] = strawberry.field(description="The list of pokemons types")
    metadata: PageMeta = strawberry.field(description="Metadata")