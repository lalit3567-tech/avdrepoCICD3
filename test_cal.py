import pytest
from cal import add, subtract, multiply, divide


def test_add(a,b):
    assert add(10,20) == 30

def test_sub(a,b):
    assert subtract(20,10) == 10

def test_mul(a,b):
    assert multiply(10,20) == 200
    

def test_div(a,b):
    assert divide(20,10) == 2