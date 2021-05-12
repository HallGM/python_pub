import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Gin and Tonic", 5, 5)

    def test_get_price(self):
        self.assertEqual(5, self.drink.get_price())
