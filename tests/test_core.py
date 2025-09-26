import pytest
from core import Operation, calculate, parse_operation

def test_add():
    assert calculate(2, 3, Operation.ADD) == 5

def test_sub():
    assert calculate(5, 1, Operation.SUB) == 4

def test_mul():
    assert calculate(2, 5, Operation.MUL) == 10

def test_div():
    assert calculate(10, 2, Operation.DIV) == 5

def test_pow():
    assert calculate(2, 3, Operation.POW) == 8

def test_add_floating():
    assert calculate(2.5, 1.7, Operation.ADD)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(2, 0, Operation.DIV)

def test_div_zero():
    assert calculate(0, 5, Operation.DIV) == 0

def test_mul_zero():
    assert calculate(5, 0, Operation.MUL) == 0

def test_negative_result():
    assert calculate(2, 5, Operation.SUB) == -3

def test_pow_floating():
    assert calculate(2.5, 1.7, Operation.POW)

def test_pow_zero():
    assert calculate(100, 0, Operation.POW) == 1

def test_invalid_operation():
    with pytest.raises(ValueError):
        parse_operation("invalid_operation")


