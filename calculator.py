#!/usr/bin/env python3
"""
Простой калькулятор для практической работы по Git.
Поддерживает операции: сложение, вычитание, умножение, деление.
"""

def add(x, y):
    """Возвращает сумму двух чисел."""
    return x + y

def subtract(x, y):
    """Возвращает разность двух чисел (x - y)."""
    return x - y

def multiply(x, y):
    """Возвращает произведение двух чисел."""
    return x * y

def divide(x, y):
    """
    Возвращает частное двух чисел (x / y).
    Если y равен нулю, выбрасывает исключение.
    """
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

def main():
    """Основная функция программы."""
    print("Добро пожаловать в простой калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        # Получаем выбор пользователя
        choice = input("\nВведите номер операции (1/2/3/4) или 'q' для выхода: ")

        if choice == 'q':
            print("Выход из программы.")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 4.")
            continue

        try:
            # Получаем числа от пользователя
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите корректное число.")
            continue

        # Выполняем выбранную операцию
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            try:
                result = divide(num1, num2)
                operation = "/"
            except ValueError as e:
                print(f"Ошибка: {e}")
                continue

        print(f"Результат: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
