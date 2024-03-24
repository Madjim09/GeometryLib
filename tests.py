import unittest
from area import circle, triangle
from checks import is_right_triangle


class TestGeometryLibrary(unittest.TestCase):
    def test_circle_area(self):
        # Проверяем, что площадь круга с радиусом 1 правильно вычисляется
        self.assertAlmostEqual(circle(1), 3.141592653589793, places=10)

        # Проверяем, что площадь круга с радиусом 0 правильно вычисляется
        self.assertAlmostEqual(circle(0), 0)

        # Проверяем, что площадь круга с отрицательным радиусом вызывает исключение ValueError
        with self.assertRaises(ValueError):
            circle(-1)

    def test_triangle_area(self):
        # Проверяем, что площадь треугольника с сторонами 3, 4, 5 правильно вычисляется
        self.assertAlmostEqual(triangle(3, 4, 5), 6)

        # Проверяем, что площадь треугольника с сторонами 6, 8, 10 правильно вычисляется
        self.assertAlmostEqual(triangle(6, 8, 10), 24)

        # Проверяем, что площадь треугольника с отрицательными сторонами вызывает исключение ValueError
        with self.assertRaises(ValueError):
            triangle(-3, 4, 5)

    def check_right_angled_triangle(self):
        def test_right_triangle(self):
            # Проверка для треугольника со сторонами 3, 4, 5
            self.assertTrue(is_right_triangle(3, 4, 5))
            # Проверка для треугольника со сторонами 5, 12, 13
            self.assertTrue(is_right_triangle(5, 12, 13))

        def test_not_right_triangle(self):
            # Проверка для треугольника со сторонами 3, 4, 6
            self.assertFalse(is_right_triangle(3, 4, 6))
            # Проверка для треугольника со сторонами 1, 1, 1
            self.assertFalse(is_right_triangle(1, 1, 1))
            # Проверка для треугольника со сторонами 5, 5, 5
            self.assertFalse(is_right_triangle(5, 5, 5))

        def test_negative_sides(self):
            # Проверка для треугольника со отрицательной стороной
            with self.assertRaises(ValueError):
                is_right_triangle(-3, 4, 5)


if __name__ == '__main__':
    unittest.main()