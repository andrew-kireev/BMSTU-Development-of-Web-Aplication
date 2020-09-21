import math
from lab_python_oop.Figure_color import Figure_color
from lab_python_oop.geometric_figure import Figure

class Circle(Figure):
    def __init__(self, radius, color):
        TYPE = 'Circle'
        self.radius = radius
        self.color = Figure_color()
        self.color.color = color


    @classmethod
    def get_type(cls):
        return cls.TYPE

    def square(self):
        return self.radius * self.radius * math.pi

    def __repr__(self):
        return 'Circle radius = {}, color = {}, square = {}'.format(
            self.radius,
            self.color.color,
            self.square()
        )