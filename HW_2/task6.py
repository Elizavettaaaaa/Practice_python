# Горохова Е.С.
# Задача 6. Банкомат: PIN-код

PIN = 1234
attempts_left = 3

while attempts_left > 0:
    entered = int(input("Введите PIN: "))

    if entered == PIN:
        print("Доступ разрешён")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Неверный PIN. Осталось попыток: {attempts_left}")
        else:
            print("Карта заблокирована")