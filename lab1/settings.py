def set_decimal_precision():
    while True:
        try:
            precision = int(input("Введіть кількість десяткових знаків (0-10): "))
            if 0 <= precision <= 10:
                return precision
            else:
                print("Будь ласка, введіть число від 0 до 10.")
        except ValueError:
            print("Помилка: Введіть ціле число.")
