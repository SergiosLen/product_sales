import unittest

from message_process import helpers

class ProductTest(unittest.TestCase):
    def setUp(self):
        self.product= helpers.Product('apple','30p')

    def test_add_operation(self):

        self.product.add_to_price(20)
        self.assertEqual(self.product.price,50)

    def test_subtract_operation(self):

        self.product.subtract_to_price(20)
        self.assertEqual(self.product.price,10)

    def test_multiply_operation(self):

        self.product.multiply_to_price(2)
        self.assertEqual(self.product.price,60)
    @unittest.skip('If not zero valid multiplier')
    def test_multiply_with_0(self):
        self.assertRaises('Value Error 0 as a multiplier is not valid!')


if __name__ == '__main__':
    unittest.main()