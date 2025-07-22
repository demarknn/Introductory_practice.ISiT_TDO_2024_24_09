import math

def calculate_factorial(n):
    """Вычисляет факториал числа n с использованием math.factorial для оптимизации."""
    return math.factorial(n)

def main():
    print("Программа для вычисления факториала числа.")
    try:
        # Запрос ввода от пользователя
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)

        # Проверка на отрицательное число
        if number < 0:
            print("Ошибка: Факториал отрицательного числа не определен.")
            return

        # Вычисление факториала
        result = calculate_factorial(number)
        print(f"Факториал числа {number} равен: {result}")

    except ValueError:
        print("Ошибка: Введено нечисловое значение или нецелое число.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
