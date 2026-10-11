import unittest
from webcalc.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(5, 3), 2)

    def test_mut(self):
        self.assertEqual(self.calc.mut(4, 3), 12)

    def test_div(self):
        self.assertEqual(self.calc.div(10, 2), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.div(5, 0)

if __name__ == '__main__':
    unittest.main()