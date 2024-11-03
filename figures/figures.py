class Shape:
    """Геометрические фигуры"""

    name = "геометрическая фигура"

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{self.name} по координатам ({self.__x}, {self.__y})"


class Rectangle(Shape):
    """Прямоугольники"""

    name = "прямоугольник"

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (
            f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
            f" с площадью {self.area()} и периметром {self.perimeter()}"
        )


class Square(Rectangle):
    """Квадраты"""

    name = "квадрат"

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    def __repr__(self):
        return (
            f"{Shape.__repr__(self)}, со стороной {self.width},"
            f" с площадью {self.area()} и периметром {self.perimeter()}"
        )
