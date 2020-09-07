import math
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

    def calculate(self):
        is_two_root = False
        discr = self.b ** 2 - 4 * self.a * self.c
        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
        elif discr == 0:
            x = -self.b / (2 * self.a)
            is_two_root = True
        else:
            print("No roots((!")
        if not is_two_root:
            root1 = math.sqrt(x1)
            root2 = -math.sqrt(x1)
            root3 = math.sqrt(x2)
            root4 = -math.sqrt(x2)
            print('x1 = ' + str(root1) + ' x2 = ' + str(root2) +
                  ' x3 = ' + str(root3) + ' x4 = ' + str(root4))
        else:
            root1 = math.sqrt(x)
            root2 = -math.sqrt(x)
            print('x1 = ' + str(root1) + ' x2 = ' + str(root2))


eq = Equation()
# eq.print()
eq.calculate()
