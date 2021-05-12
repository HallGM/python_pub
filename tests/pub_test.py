import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Spritz", 8, 4)
        self.drink_2 = Drink("Gin and Tonic", 5, 5)
        self.pub = Pub("Three Bells", 100, [self.drink_1, self.drink_2])
        self.customer_1 = Customer("Garry", 10, 29)
        self.customer_2 = Customer("Adam", 15, 17)

    def test_add_money(self):
        self.pub.add_money(50)
        self.assertEqual(150, self.pub.till)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer_1))
        self.assertEqual(False, self.pub.check_age(self.customer_2))

    def test_check_is_sober(self):
        self.customer_1.buy_drink(self.drink_2, self.pub)
        self.assertEqual(True, self.pub.is_sober(self.customer_1))
        for i in range(4):
            self.customer_1.buy_drink(self.drink_2, self.pub)
        self.assertEqual(False, self.pub.is_sober(self.customer_1))
