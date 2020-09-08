import math
import cmath
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('a', nargs='?')
    parser.add_argument('b', nargs='?')
    parser.add_argument('c', nargs='?')
    return parser

class Equation:
    def __init__(self):
        parser = create_parser()
        namespace = parser.parse_args()
        if not namespace.a or not namespace.b or not namespace.c:
            self.a = float(input())
            self.b = float(input())
            self.c = float(input())
        else:
            self.a = float(namespace.a)
            self.b = float(namespace.b)
            self.c = float(namespace.c)

    def print(self):
        print('a = ' + str(self.a))
        print('b = ' + str(self.b))
        print('c = ' + str(self.c))

    def three_argc(self):
        # ax^4 + bx^2 + c = 0
        is_two_root = False
        discr = self.b ** 2 - 4 * self.a * self.c
        if discr > 0:
            x1 = (-self.b + cmath.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - cmath.sqrt(discr)) / (2 * self.a)
        elif discr == 0:
            x = -self.b / (2 * self.a)
            is_two_root = True
        else:
            print("No roots((!")
        if not is_two_root:
            root1 = cmath.sqrt(x1)
            root2 = -cmath.sqrt(x1)
            root3 = cmath.sqrt(x2)
            root4 = -cmath.sqrt(x2)
            print('x1 = ' + str(root1) + ' x2 = ' + str(root2) +
                  ' x3 = ' + str(root3) + ' x4 = ' + str(root4))
        else:
            root1 = cmath.sqrt(x)
            root2 = -cmath.sqrt(x)
            print('x1 = ' + str(root1) + ' x2 = ' + str(root2))

    def c_zero(self):
        # ax^4 + bx^2 = 0
        if self.b > 0:
            x = cmath.sqrt(b / a)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))
        else:
            x = cmath.sqrt(-b / a)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))

    def b_zero(self):
        # ax^4 + c = 0
        if c > 0:
            x = cmath.sqrt(c / a)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))
        else:
            x = cmath.sqrt(-c / a)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))

    def a_zero(self):
         # bx^2 + c = 0
        if c > 0:
            x = cmath.sqrt(c / b)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))
        else:
            x = cmath.sqrt(-c / b)
            print('x1 = ' + str(x) + ' x2 = ' + str(-x))

    def b_and_c_zero(self):
        print('x1 = 0 x2 = 0 x3 = 0 x4 = 0')

    def a_and_c_zero(self):
        print('x1 = 0 x2 = 0')

    def calculate(self):
        if self.a != 0 and self.b != 0 and self.c != 0:
            self.three_argc()
        elif self.a != 0 and self.b != 0 and self.c == 0:
            self.c_zero()
        elif self.a != 0 and self.c != 0 and self.b == 0:
            self.b_zero()
        elif self.b != 0 and self.c != 0 and self.a == 0:
            self.a_zero
        elif self.a != 0 and self.b == 0 and self.c == 0:
            self.b_and_c_zero()
        elif self.b != 0 and self.a == 0 and self.c == 0:
            self.a_and_c_zero()
        else:
            print('infinite amount of roots')


eq = Equation()
# eq.print()
eq.calculate()
