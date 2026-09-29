# Горохова Е.С.
# Задача 1. Знак и чётность числа

number = int(input("Введите число: "))

# Определяем знак
if number > 0:
    sign = "Положительное"
elif number < 0:
    sign = "Отрицательное"
else:
    sign = "Ноль"

# Определяем чётность (ноль считаем чётным)
if number % 2 == 0:
    parity = "чётное"
else:
    parity = "нечётное"

print(sign, parity)