import unittest

import ingredient
import recipe

INGREDIENTS = {
    'parsley': ingredient.Ingredient("Parsley"),
    'avocado': ingredient.Ingredient("Avocado"),
    'tomato': ingredient.Ingredient("Tomato"),
    'onion': ingredient.Ingredient("Onion"),
}


class RecipeIngredientTestCase(unittest.TestCase):
    def test_basic_ingredient(self):
        ri = recipe.RecipeIngredient(INGREDIENTS['parsley'], 2, 'tbsp')
        self.assertIs(ri.ingredient, INGREDIENTS['parsley'])
        self.assertEquals(ri.quantity, 2)
        self.assertEquals(ri.measurement, 'tbsp')

    def test_create_ingredient(self):
        ri = recipe.RecipeIngredient('parsley', 2, 'tbsp')
        self.assertIsNot(ri.ingredient, INGREDIENTS['parsley'])

    def test_with_condition(self):
        ri = recipe.RecipeIngredient(INGREDIENTS['parsley'], 2,
                                     'tbsp', 'finely chopped')
        self.assertEqual(ri.condition, 'finely chopped')

    def test_str_with_condition(self):
        ri = recipe.RecipeIngredient(INGREDIENTS['parsley'], 2,
                                     'tbsp', 'finely chopped')
        self.assertEquals(
            str(ri),
            f'{ri.quantity} {ri.measurement} {ri.ingredient} ({ri.condition})'
        )

    def test_str_without_condition(self):
        ri = recipe.RecipeIngredient(INGREDIENTS['parsley'], 2, 'tbsp')
        self.assertEquals(
            str(ri),
            f'{ri.quantity} {ri.measurement} {ri.ingredient}'
        )


class RecipeStepTestCase(unittest.TestCase):
    def test_basic(self):
        text = "Use a fork to smooth the mixture"
        rs = recipe.RecipeStep(text)
        self.assertEqual(rs.text, text)
        self.assertEqual(str(rs), text)


class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.ingredients = [
            recipe.RecipeIngredient(INGREDIENTS['parsley'], 2, 'tbsp', 'chopped'),
            recipe.RecipeIngredient(INGREDIENTS['avocado'], 2, condition='scooped out'),
            recipe.RecipeIngredient(INGREDIENTS['tomato'], 3, condition='diced'),
            recipe.RecipeIngredient(INGREDIENTS['onion'], 0.5, condition='diced'),
        ]
        self.steps = [
            recipe.RecipeStep("Add all ingredients to a bowl"),
            recipe.RecipeStep("Stir to combine and smooth"),
            recipe.RecipeStep("Add salt and pepper to taste"),
            recipe.RecipeStep("Wash all ingredients"),
        ]
        self.recipe = recipe.Recipe("Guacamole")

    def test_basic_creation(self):
        title = "Guacamole"
        r = recipe.Recipe(title)
        self.assertEqual(r.title, title)

    def test_add_ingredient_pieces(self):
        self.recipe.add_ingredient(INGREDIENTS['parsley'], 2, 'tbsp')
        self.assertEqual(len(self.recipe.ingredients), 1)
        self.assertEqual(
            self.recipe.ingredients[0].ingredient.name,
            'Parsley'
        )

    def test_add_ingredient_whole(self):
        self.recipe.add_ingredient(self.ingredients[0])
        self.assertEqual(len(self.recipe.ingredients), 1)
        self.assertEqual(
            self.recipe.ingredients[0].ingredient.name,
            'Parsley'
        )
        self.assertIs(self.recipe.ingredients[0], self.ingredients[0])

    def test_add_step_text(self):
        self.recipe.add_step("Wash everything")
        self.assertEqual(self.recipe.steps[0].text, "Wash everything")

    def test_add_prepared_step(self):
        self.recipe.add_step(self.steps[0])
        self.assertIs(self.recipe.steps[0], self.steps[0])

    def test_add_step_with_order(self):
        self.recipe.add_step(self.steps[0])
        self.recipe.add_step(self.steps[-1], 0)
        self.assertEqual(self.recipe.steps[0], self.steps[-1])


