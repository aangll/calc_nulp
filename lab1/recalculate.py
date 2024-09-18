def ask_for_repeat():
    while True:
        answer = input("Чи хочете виконати ще одне обчислення? (так/ні): ").lower()
        if answer in ['так', 'ні']:
            return answer == 'так'
        print("Будь ласка, введіть 'так' або 'ні'.")
