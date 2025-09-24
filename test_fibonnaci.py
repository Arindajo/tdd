import pytest
from fibonnaci import fibonacci


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_negative_input_raises_error():
    with pytest.raises(ValueError):
        fibonacci(-3)
