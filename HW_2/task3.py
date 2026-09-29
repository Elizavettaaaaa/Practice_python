# Горохова Е.С.
# Задача 3. Сумма чисел до нуля

total = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    total += number

print("Сумма:", total)