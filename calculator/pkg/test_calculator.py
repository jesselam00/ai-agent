
import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        result = calc.evaluate("3 + 2")
        print(f"Addition result: {result}")
        self.assertEqual(result, 5)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.evaluate("3 - 2")
        print(f"Subtraction result: {result}")
        self.assertEqual(result, 1)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.evaluate("3 * 2")
        print(f"Multiplication result: {result}")
        self.assertEqual(result, 6)

    def test_division(self):
        calc = Calculator()
        result = calc.evaluate("6 / 2")
        print(f"Division result: {result}")
        self.assertEqual(result, 3)

    def test_precedence(self):
        calc = Calculator()
        result = calc.evaluate("3 + 7 * 2")
        print(f"Precedence result: {result}")
        self.assertEqual(result, 17)

    def test_complex(self):
        calc = Calculator()
        result = calc.evaluate("3 + 7 * 2 - 10 / 5")
        print(f"Complex result: {result}")
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
