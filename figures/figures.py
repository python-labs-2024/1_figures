class Shape:
    """Геометрические фигуры"""

    name = "геометрическая фигура"

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name} по координатам ({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"


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

    def __str__(self):
        return (
            f"{super().__str__()}, со сторонами {self.width} и {self.height},"
            f" с площадью {self.area()} и периметром {self.perimeter()}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(width={self.width}, height={self.height},"
            f" x={self.x}, y={self.y})"
        )


class Square(Rectangle):
    """Квадраты"""

    name = "квадрат"

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, value):
        self.width = self.height = value

    def __str__(self):
        return (
            f"{super(Rectangle, self).__str__()}, со стороной {self.side},"
            f" с площадью {self.area()} и периметром {self.perimeter()}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.side}, x={self.x}, y={self.y})"
