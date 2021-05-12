import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Garry", 10, 29)
        self.customer_2 = Customer("Adam", 15, 17)
        self.drink_1 = Drink("Spritz", 8, 4)
        self.drink_2 = Drink("Gin and Tonic", 5, 5)
        self.pub = Pub("Three Bells", 100, [self.drink_1, self.drink_2])

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink_2, self.pub)
        self.assertEqual(5, self.customer.wallet)
        self.assertEqual(105, self.pub.till)

    def test_check_age_before_buy_drink(self):
        self.customer_2.buy_drink(self.drink_2, self.pub)
        self.assertEqual(15, self.customer_2.wallet)
        self.assertEqual(100, self.pub.till)

    def test_increment_drunkenness(self):
        self.customer.increment_drunkenness(self.drink_1)
        self.assertEqual(4, self.customer.drunkenness)

    def test_buy_drink_increase_drunkenness(self):
        self.customer.buy_drink(self.drink_1, self.pub)
        self.assertEqual(4, self.customer.drunkenness)
