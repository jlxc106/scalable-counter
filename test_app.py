import pytest

def f(x):
    return x+1

def test_answer():
    assert f(3) == 4