# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, A, B, C):
        def side(X, Y):
            return ((Y[0] - X[0])**2 + (Y[1] - X[1])**2)**0.5

        self.A = A
        self.B = B
        self.C = C

        self.a = side(A, B)
        self.b = side(B, C)
        self.c = side(C, A)

    # Периметр
    def perimeter(self):
        return self.a + self.b + self.c

    # Площадь
    def square(self):
        __p = (self.perimeter()) * 0.5
        return (__p * (__p - self.a) * (__p - self.b) * (__p - self.c)) ** 0.5

    # Высота
    def height(self):
        __ha = (2 * self.square()) / self.a
        __hb = (2 * self.square()) / self.b
        __hc = (2 * self.square()) / self.c
        return __ha, __hb, __hc

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

class EqualTrapezoid:
    def __init__(self, A, B, C, D):
        def side(X, Y):
            return ((Y[0] - X[0])**2 + (Y[1] - X[1])**2)**0.5

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.a = side(A, B)
        self.b = side(B, C)
        self.c = side(C, D)
        self.d = side(D, A)


    # Периметр
    def perimeter(self):
        return self.a + self.b + self.c + self.d

    # Площадь
    def square(self):
        return ((self.b + self.d) / 2) * (((self.a ** 2) - (((((self.d - self.b) ** 2) + (self.a ** 2) - (self.c ** 2)) / (2 * (self.d - self.b))) ** 2)) ** 0.5)

    # Высота
    def height(self):
        return ((self.a ** 2) - (((((self.d - self.b) ** 2) + (self.a ** 2) - (self.c ** 2)) / (2 * (self.d - self.b))) ** 2)) ** 0.5

    def check(self):
        # Проверяем равенство сторон трапеции
        if self.a != self.c:
            return False

        # Проверяем равенство углов трапеции
        # Не нащёл понятной формулы по вычислению углов

        return True

# Проверка
if __name__ == '__main__':
    test1 = Triangle([1, 1], [2, 2], [3, 1])

    print(test1.A, test1.B, test1.C, test1.a, test1.b, test1.c)
    print('Периметр\t= ', test1.perimeter())
    print('Площадь\t\t= ', test1.square())
    print('Высота\t\t= ', test1.height())

    test2 = EqualTrapezoid([0, 0], [2, 2], [4, 2], [6, 0])

    print(test2.A, test2.B, test2.C, test2.D, test2.a, test2.b, test2.c, test2.d)
    print('Периметр\t= ', test2.perimeter())
    print('Площадь\t\t= ', test2.square())
    print('Высота\t\t= ', test2.height())
    print(test2.check())