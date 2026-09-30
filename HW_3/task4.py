# Упражнение 4. Десятичный счётчик

class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

    def get_counter(self):
        return self.value


if __name__ == "__main__":
    c = Counter()
    c.increment()
    c.increment()
    c.increment()
    print(c.get_counter())  # 3
    c.decrement()
    print(c.get_counter())  # 2
    c.decrement()
    c.decrement()
    c.decrement()
    print(c.get_counter())  # 0, ниже не опускается