from math import pi, sqrt


def circle(radius: [int, float]) -> [int, float]:
    '''
    Считает площадь окружности по ее радиусу
    Радиус      :param radius:  [int, float]
    Площадь(S)  :return:        [int, float]
    '''
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return pi * (radius ** 2)


def triangle(a: [int, float], b: [int, float], c: [int, float]) -> [int, float]:
    '''
    Считает полощадь треугольника по трем его сторонам
    1 сторона   :param a:   [int, float]
    2 сторона   :param b:   [int, float]
    3 сторона   :param c:   [int, float]
    Площадь(S)  :return:    [int, float]
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Длины сторон не могут быть отрицательными")
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))