# TASK 2

import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Consider me implemented", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


# After implementation, I created an instance for each new class and printed out the results of calc_perimeter method.

rectangle = Rectangle(2, 6)
rectangle_result = rectangle.calc_perimeter()
print(rectangle_result)

square = Square(4)
square_result = square.calc_perimeter()
print(square_result)
