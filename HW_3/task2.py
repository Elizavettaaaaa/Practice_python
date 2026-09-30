# Упражнение 2. Класс Rectangle: площадь и периметр

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def width(self):
        return self.top_right.x - self.bottom_left.x

    def height(self):
        return self.top_right.y - self.bottom_left.y

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return 2 * (self.width() + self.height())


if __name__ == "__main__":
    r = Rectangle(Point(0, 0), Point(4, 3))
    print("Площадь:", r.area())
    print("Периметр:", r.perimeter())