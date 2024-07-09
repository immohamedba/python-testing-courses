import math
import source.Shapes as Shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        result = self.circle.area()
        assert result == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 2 * math.pi * self.circle.radius

    def test_not_in_the_area(self, my_rectangle):
        assert self.circle.area() != self.my_rectangle.area()
