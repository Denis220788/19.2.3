import pytest
from calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_culcalate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_substraction_calculate_correctly(self):
        assert self.calc.substraction(self, 9, 3) == 6

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 5) == 9