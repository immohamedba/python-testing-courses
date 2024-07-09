import time

import pytest

import source.my_functions as my_functions


def test_add():
    result = my_functions.add(2, 2)
    assert result == 5


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(5, 0)


def test_add_string():
    result = my_functions.add_string("I like", "learning")
    assert result == "I like learning"


@pytest.mark.xfail(reason="we know we can't divide by zero")
def test_divide_by_zero_broken():
    my_functions.divide(5, 0)


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(4, 4) == 18


@pytest.mark.slow()
def test_slow_mark():
    time.sleep(5)
    assert 2 * 5 == 10
