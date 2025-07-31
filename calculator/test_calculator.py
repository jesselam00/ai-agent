
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("3 + 2"), 5)

    def test_subtraction(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("3 - 2"), 1)

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("3 * 2"), 6)

    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("6 / 2"), 3)

    def test_precedence(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("3 + 7 * 2"), 17)

    def test_complex(self):
        calc = Calculator()
        self.assertEqual(calc.evaluate("3 + 7 * 2 - 10 / 5"), 15)

if __name__ == '__main__':
    unittest.main()
