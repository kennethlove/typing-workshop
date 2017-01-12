import unittest

import ingredient


class IngredientTestCase(unittest.TestCase):
    def test_str(self):
        ing = ingredient.Ingredient("Parsley")
        self.assertEqual(str(ing), "Parsley")