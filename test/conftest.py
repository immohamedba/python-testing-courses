import pytest
import source.Shapes as Shapes


@pytest.fixture()
def my_rectangle():
    return Shapes.Rectangle(10, 5)


@pytest.fixture()
def weird_rectangle():
    return Shapes.Rectangle(5, 10)