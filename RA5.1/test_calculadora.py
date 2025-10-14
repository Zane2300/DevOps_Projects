import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)
        self.assertEqual(self.calc.multiplicar(0, 99), 0)
        self.assertAlmostEqual(self.calc.multiplicar(2.5, 4), 10.0)

if __name__ == "__main__":
    unittest.main()
