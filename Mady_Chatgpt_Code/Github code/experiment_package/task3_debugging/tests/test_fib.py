from buggy import fib

def test_base():
    assert fib(1) == 1

def test_ten():
    assert fib(10) == 55

def test_thirty():
    assert fib(30) == 832040
