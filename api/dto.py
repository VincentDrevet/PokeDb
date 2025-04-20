import strawberry

@strawberry.type
class PokemonType:
    id: int
    name: str
    hp: int
    generation: int
    legendary: bool
