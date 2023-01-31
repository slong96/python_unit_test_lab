import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

     # test list of 1 prices
    def test_list_of_two_prices(self):
        prices = [10]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    # test list of 2 prices
    def test_list_of_two_prices(self):
        prices = [3, 20]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    # test empty list
    def test_empty_price_list(self):
        prices = []
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    # test if price is greater than zero
    def test_list_prices_greater_than_zero(self):
        prices = [9, 4, 6, 7, 3]
        self.assertGreater(discount(prices), 0)

    # test floats
    def test_floats(self):
        prices = [10.99, 4.99, 19,99]
        expected_discount = 4.99
        self.assertEqual(expected_discount, discount(prices))
        

if __name__ == '__main__':
    unittest.main()