# Упражнение 1. Класс Point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    p = Point(3, 5)
    print(p)