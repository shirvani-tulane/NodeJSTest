# test_fibonacci.py

from fibonacci import fibonacci  # if your function is in fibonacci.py

def test_fibonacci_5():
    """Test that fibonacci(5) returns the first five Fibonacci numbers."""
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_1():
    """Test that fibonacci(1) returns only the first Fibonacci number."""
    assert fibonacci(1) == [0]


def test_fibonacci_0():
    """Test that fibonacci(0) returns an empty list."""
    assert fibonacci(0) == []
