import pytest
from source import Shapes as shapes


@pytest.mark.parametrize("side_length,expected_area", [(4, 16), (5, 25), (3, 9)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(2, 8), (3, 12), (5, 20)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
