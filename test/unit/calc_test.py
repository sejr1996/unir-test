import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True

def mocked_validation_false(*args, **kwargs):
    return False

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(11, self.calc.add(5, 6))
        self.assertEqual(210, self.calc.add(140, 70))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(18, self.calc.substract(20, 2))
        self.assertEqual(24, self.calc.substract(12, -12))
        self.assertEqual(32, self.calc.substract(33, 1))
        self.assertEqual(10, self.calc.substract(10, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "None")
        self.assertRaises(TypeError, self.calc.substract, 12, object())

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(10, self.calc.divide(50, 5))
        self.assertEqual(1, self.calc.divide(20, 20))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation_false, create=True)
    def test_multiply_method_fails_validation_permissions(self, _validate_permissions):
        self.assertRaises(Exception, self.calc.multiply, 2, 2)
        self.assertRaises(Exception, self.calc.multiply, 1, 0)

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "3", 2)
        self.assertRaises(TypeError, self.calc.multiply, 1, None)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        self.assertRaises(TypeError, self.calc.multiply, None, "2")

    def test_power_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.power(0, 4))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(64, self.calc.power(4, 3))
        self.assertEqual(100, self.calc.power(10, 2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(10, self.calc.sqrt(100))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(3, self.calc.log10(1000))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "100")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
