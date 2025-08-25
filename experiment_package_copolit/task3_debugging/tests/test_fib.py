from experiment_package.task3_debugging.buggy import fib #  Adjust import to remove error in test file 
import pytest

def test_zero():
    assert fib(0) == 0

def test_base():
    assert fib(1) == 1

def test_ten():
    assert fib(10) == 55

def test_thirty():
    assert fib(30) == 832040

def test_invalid():
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(ValueError):
        fib(2.5)