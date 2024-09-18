history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if history:
        print("Історія обчислень:")
        for entry in history:
            print(entry)
    else:
        print("Історія порожня.")
