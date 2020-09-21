from lab_python_oop.Figure_color import Figure_color
from lab_python_oop.geometric_figure import Figure

class Square(Figure):
    def __init__(self, side, color):
        TYPE = 'Circle'
        self.side = side
        self.color = Figure_color()
        self.color.color = color


    @classmethod
    def get_type(cls):
        return cls.TYPE

    def square(self):
        return self.side * self.side

    def __repr__(self):
        return 'Square side = {}, color = {}'.format(
            self.side,
            self.color.color
        )