from figures import Rectangle, Square


def test_rectangle_area():
    probationers_1 = Rectangle(3, 5)

    assert probationers_1.area() == 15

    probationers_2 = Rectangle(3, 0)
    assert probationers_2.area() == 0

    probationers_3 = Rectangle(0, 3)
    assert probationers_3.area() == 0

    probationers_4 = Rectangle(1, 1)
    assert probationers_4.area() == 1

    probationers_5 = Rectangle(1, 3)
    assert probationers_5.area() == 3

    probationers_6 = Rectangle(3, 1)
    assert probationers_6.area() == 3


def test_rectangle_perimeter():
    probationers_1 = Rectangle(3, 5)

    assert probationers_1.perimeter() == 16

    probationers_2 = Rectangle(3, 0)
    assert probationers_2.perimeter() == 6

    probationers_3 = Rectangle(0, 3)
    assert probationers_3.perimeter() == 6

    probationers_4 = Rectangle(0, 0)
    assert probationers_4.perimeter() == 0

    probationers_5 = Rectangle(1, 1)
    assert probationers_5.perimeter() == 4

    probationers_6 = Rectangle(1, 3)
    assert probationers_6.perimeter() == 8

    probationers_7 = Rectangle(3, 1)
    assert probationers_7.perimeter() == 8


def test_square_area():
    probationers_1 = Square(3)

    assert probationers_1.area() == 9

    probationers_2 = Square(1)

    assert probationers_2.area() == 1

    probationers_3 = Square(0)

    assert probationers_3.area() == 0


def test_square_perimeter():
    probationers_1 = Square(3)

    assert probationers_1.perimeter() == 12

    probationers_2 = Square(1)

    assert probationers_2.perimeter() == 4

    probationers_3 = Square(0)

    assert probationers_3.perimeter() == 0

def test_square_modify_parameters():
    probationers_1 = Square(3)

    assert probationers_1.area() == 9
    assert probationers_1.perimeter() == 12

    probationers_1.width = 2

    assert probationers_1.area() == 4
    assert probationers_1.perimeter() == 8

    probationers_1.height = 5

    assert probationers_1.area() == 25
    assert probationers_1.perimeter() == 20


def test_liskov():
    probationers_1 = Rectangle(3, 3)
    probationers_2 = Square(3)

    assert probationers_1.area() == probationers_2.area()
    assert probationers_1.perimeter() == probationers_2.perimeter()
