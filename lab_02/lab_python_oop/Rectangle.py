from lab_python_oop.Figure_color import Figure_color
from lab_python_oop.geometric_figure import Figure

class Rectangle(Figure):
    def __init__(self, width, height, color):
        TYPE = "Rectangle"
        self.width = width
        self.height = height
        self.color = Figure_color()
        self.color.color = color

    @classmethod
    def get_type(cls):
        return cls.TYPE

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return 'Rectangle width = {}, height = {}, color = {}'.format(
            self.width,
            self.height,
            self.color.color
        )

