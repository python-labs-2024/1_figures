from figures import Rectangle, Square


def test_rectangle():
    probationers_1 = Rectangle(3, 5)

    assert probationers_1.area() == 15
    assert probationers_1.perimeter() == 16


def test_square():
    probationers_2 = Square(3)

    assert probationers_2.area() == 9
    assert probationers_2.perimeter() == 12

    probationers_2.width = 2
    assert probationers_2.area() == 4
    assert probationers_2.perimeter() == 8

    probationers_2.height = 5
    assert probationers_2.area() == 25
    assert probationers_2.perimeter() == 20

def test_liskov():
    probationers_1 = Rectangle(3, 3)
    probationers_2 = Square(3)

    assert probationers_1.area() == probationers_2.area()
    assert probationers_1.perimeter() == probationers_2.perimeter()
