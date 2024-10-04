import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc=SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10,5),15)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(0,0),0)
        self.assertEqual(self.calc.add(-1,-1),-2)

    def test_subtraction(self):
        self.assertNotEqual(self.calc.subtract(1,-1),1)
        self.assertEqual(self.calc.subtract(10,10),0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(1,0),0)
        self.assertEqual(self.calc.multiply(1000,1000),1000000)

    def test_division(self):
        self.assertIsNotNone(self.calc.divide(1,0))
        self.assertEqual(self.calc.divide(10,2),5)

