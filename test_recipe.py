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


