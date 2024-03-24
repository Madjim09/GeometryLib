def is_right_triangle(a: [int, float], b: [int, float], c: [int, float]) -> bool:
    '''
    Возвращает True если треугольник является прямоугольным, иначе False
    1 сторона           :param a:   [int, float]
    2 сторона           :param b:   [int, float]
    3 сторона           :param c:   [int, float]
    Результат проверки  :return:    bool
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Длины сторон не могут быть отрицательными")
    mas = [a, b, c]
    gip = max(a, b, c)
    mas.remove(gip)
    return gip ** 2 == (mas[0] ** 2) + (mas[1] ** 2)
