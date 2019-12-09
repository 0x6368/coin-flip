import unittest
import bit
from dealer import Dealer


class MyTest(unittest.TestCase):
    def test_nth_bit(self):
        self.assertEqual(bit.nth_bit(0b0000, 0, 4), 0)
        self.assertEqual(bit.nth_bit(0b1000, 0, 4), 1)
        self.assertEqual(bit.nth_bit(0b1100, 0, 4), 1)
        self.assertEqual(bit.nth_bit(0b0100, 0, 4), 0)
        self.assertEqual(bit.nth_bit(0b0100, 0, 3), 1)
        self.assertEqual(bit.nth_bit(0b0100, 0, 2), 0)

    def test_dealer_estimation(self):
        value = Dealer.get_estimated_inner_value(0b000111, 3, 6)
        self.assertEqual(value, 1.5)
