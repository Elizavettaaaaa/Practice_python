# Горохова Е.С.
# Задача 7. Касса магазина

total = 0

while True:
    price = float(input("Цена товара: "))

    if price < 0:
        print("Цена не может быть отрицательной")
        continue

    if price == 0:
        break

    total += price

print(f"Сумма: {total:.0f} руб.")

if total >= 1000:
    discount = total * 0.10
    final = total - discount
    print(f"Скидка 10%: {discount:.0f} руб.")
    print(f"К оплате: {final:.0f} руб.")
else:
    print("Скидка: нет")
    print(f"К оплате: {total:.0f} руб.")