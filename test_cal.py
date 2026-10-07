import pytest
from cal import add, subtract, multiply, divide


def test_add():
    assert add(10,20) == 30

def test_sub():
    assert subtract(20,10) == 10

# def test_mul():
#     assert multiply(10,20) == 200
    

# def test_div():
#     assert divide(20,10) == 2