class Ingredient:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self) -> str:
        return self.name