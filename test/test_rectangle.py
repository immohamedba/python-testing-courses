def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 5


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (5 * 2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
