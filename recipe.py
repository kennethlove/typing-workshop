from ingredient import Ingredient


class RecipeIngredient:
    def __init__(self, ingredient, quantity, measurement=None, condition=None):
        if isinstance(ingredient, Ingredient):
            self.ingredient = ingredient
        else:
            self.ingredient = Ingredient(ingredient)
        self.quantity = quantity
        self.measurement = measurement
        self.condition = condition

    def __str__(self):
        condition = ''
        if self.condition:
            condition = f' ({self.condition})'
        if self.measurement:
            amount = f'{self.quantity} {self.measurement}'
        else:
            amount = self.quantity
        return f'{amount} {self.ingredient}{condition}'


class RecipeStep:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []
        self.steps = []

    def __str__(self):
        return (f'{self.title}: {len(self.ingredients)} ingredients, '
                f'{len(self.steps)} steps')

    def add_ingredient(self, ingredient, quantity=None, measurement=None, condition=None):
        if isinstance(ingredient, RecipeIngredient):
            self.ingredients.append(ingredient)
        else:
            assert quantity
            self.ingredients.append(
                RecipeIngredient(ingredient, quantity, measurement, condition)
            )

    def add_step(self, text, order=-1):
        if isinstance(text, RecipeStep):
            self.steps.insert(order, text)
        else:
            self.steps.insert(order, RecipeStep(text))

    def print(self):
        print(self.title)
        for ingredient in self.ingredients:
            print(ingredient)
        print('-'*20)
        for step in self.steps:
            print(step)

