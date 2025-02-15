import unittest
from decimal import Decimal
from calculator.calculator import Calculator, InvalidOperation


class TestCalculator(unittest.TestCase):

    def test_summ(self):
        calc = Calculator('0.1234567', '0.1')
        self.assertEqual(calc.summ(), Decimal('0.223457'))

    def test_substruct(self):
        calc = Calculator('0.3', '0.2')
        self.assertEqual(calc.substruct(), Decimal('0.1'))

    def test_multiply(self):
        calc = Calculator('10', '5')
        self.assertEqual(calc.multiply(), Decimal('50'))

    def test_divide(self):
        calc = Calculator('10', '5')
        self.assertEqual(calc.divide(), Decimal('2'))

    def test_divide_by_zero(self):
        calc = Calculator('10', '0')
        self.assertIsNone(calc.divide())

    def test_invalid_operation(self):
        with self.assertRaises(InvalidOperation):
            Calculator('invalid', Decimal('5'))

    def test_high_precision(self):
        calc = Calculator('0.1', '0.2')
        self.assertEqual(calc.summ(), Decimal('0.3'))

    def test_negative_numbers(self):
        calc = Calculator('-10', '5')
        self.assertEqual(calc.summ(), Decimal('-5'))
        self.assertEqual(calc.substruct(), Decimal('-15'))
        self.assertEqual(calc.multiply(), Decimal('-50'))
        self.assertEqual(calc.divide(), Decimal('-2'))
