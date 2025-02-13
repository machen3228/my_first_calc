import unittest
from decimal import Decimal
from calculator.calculator import summ, substruct, multiply, divide


class TestCalculator(unittest.TestCase):

    def tes_summ(self):
        '''summation function test'''
        self.assertEqual(summ(Decimal('10'), Decimal('5')), Decimal('15'))
        self.assertEqual(summ(Decimal('-10'), Decimal('5')), Decimal('-5'))
        self.assertEqual(summ(Decimal('0'), Decimal('0')), Decimal('0'))

    def test_substruct(self):
        '''substruction function test'''
        self.assertEqual(substruct(Decimal('10'), Decimal('5')), Decimal('5'))
        self.assertEqual(substruct(Decimal('-10'), Decimal('5')), Decimal('-15'))
        self.assertEqual(substruct(Decimal('0'), Decimal('0')), Decimal('0'))

    def test_multiply(self):
        '''multiplication function test'''
        self.assertEqual(multiply(Decimal('10'), Decimal('5')), Decimal('50'))
        self.assertEqual(multiply(Decimal('-10'), Decimal('5')), Decimal('-50'))
        self.assertEqual(multiply(Decimal('0'), Decimal('5')), Decimal('0'))

    def test_divide(self):
        '''division function test'''
        self.assertEqual(divide(Decimal('10'), Decimal('5')), Decimal('2'))
        self.assertEqual(divide(Decimal('-10'), Decimal('5')), Decimal('-2'))
        self.assertEqual(divide(Decimal('0'), Decimal('5')), Decimal('0'))
        self.assertIsNone(divide(Decimal('10'), Decimal('0')))

    def test_input(self):
        '''user input test'''
        with self.assertRaises(TypeError):
            summ('10', Decimal('5'))
        with self.assertRaises(TypeError):
            substruct(Decimal('10'), '5')
        with self.assertRaises(TypeError):
            multiply(Decimal('10'), '5')
        with self.assertRaises(TypeError):
            divide('10', Decimal('5'))
