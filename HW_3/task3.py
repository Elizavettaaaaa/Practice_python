# Упражнение 3. Метод contains в классе Rectangle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def contains(self, point):
        return (self.bottom_left.x <= point.x <= self.top_right.x and
                self.bottom_left.y <= point.y <= self.top_right.y)


if __name__ == "__main__":
    r = Rectangle(Point(0, 0), Point(4, 3))
    print(r.contains(Point(2, 2)))   # True
    print(r.contains(Point(5, 2)))   # False
    print(r.contains(Point(0, 0)))   # True