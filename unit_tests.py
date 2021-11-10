import unittest
import simple_calculator as cal


class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(cal.addition(10, 10), 20)
        self.assertEqual(cal.addition(10, -1), 9)
        self.assertEqual(cal.addition(-10, -10), -20)

    def test_subtraction(self):
        self.assertEqual(cal.subtraction(10, 10), 0)
        self.assertEqual(cal.subtraction(10, -1), 11)
        self.assertEqual(cal.subtraction(-10, -10), 0)

    def test_multiplication(self):
        self.assertEqual(cal.multiplication(10, 10), 100)
        self.assertEqual(cal.multiplication(10, -1), -10)
        self.assertEqual(cal.multiplication(-10, -10), 100)
        self.assertEqual(cal.multiplication(-10, 0), 0)
