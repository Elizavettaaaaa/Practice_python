# Упражнение 6. Сложение часов с проверкой отрицательных значений

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Часы, минуты и секунды не могут быть отрицательными")
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def add_second(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.add_minute()

    def add_minute(self):
        self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.add_hour()

    def add_hour(self):
        self.hours = (self.hours + 1) % 24

    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        total = self.total_seconds() + other.total_seconds()
        hours = total // 3600 % 24
        minutes = total % 3600 // 60
        seconds = total % 60
        return Clock(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes}, {self.seconds})"


if __name__ == "__main__":
    a = Clock(10, 30, 0)
    b = Clock(5, 45, 30)
    print(a + b)  # 16:15:30

    # Проверка ошибки
    try:
        bad = Clock(0, -5, 0)
    except ValueError as e:
        print("Ошибка:", e)