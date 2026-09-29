# Горохова Е.С.
# Задача 5. Угадай число

import random

secret = random.randint(1, 20)
attempts = 0

print("Я загадал число от 1 до 20. Попробуйте угадать!")

while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1

    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print(f"Верно! Число угадано за {attempts} попытки.")
        break