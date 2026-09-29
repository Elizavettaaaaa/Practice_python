# Горохова Е.С.
# Задание В: калькулятор с двумя числами и операцией

def get_number(prompt):
    """Запрашивает число, пока пользователь не введёт корректное значение."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: это не число. Попробуйте снова.")

a = get_number("Введите первое число: ")
b = get_number("Введите второе число: ")
op = input("Введите операцию (+, -, *, /, //, %): ").strip()

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
        result = None
    else:
        result = a / b
elif op == "//":
    if b == 0:
        print("Ошибка: деление на ноль")
        result = None
    else:
        result = a // b
elif op == "%":
    if b == 0:
        print("Ошибка: деление на ноль")
        result = None
    else:
        result = a % b
else:
    print("Ошибка: неизвестная операция")
    result = None

if result is not None:
    print("Результат:", result)