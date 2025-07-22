import random


def guess_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts_limit = 10
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У тебя есть {attempts_limit} попыток, чтобы угадать его.")

    while attempts < attempts_limit:
        attempts += 1
        print(f"\nПопытка №{attempts}")

        try:
            guess = int(input("Введи свое предположение: "))
        except ValueError:
            print("Пожалуйста, введи целое число!")
            continue

        if guess == secret_number:
            print(f"Поздравляю! Ты угадал число за {attempts} попыток!")
            return
        elif guess < secret_number:
            print("Мое число больше.")
        else:
            print("Мое число меньше.")

    print(f"\nК сожалению, ты исчерпал все попытки. Я загадал число {secret_number}.")


if __name__ == "__main__":
    guess_number()
    input("\nНажмите Enter для выхода...")
