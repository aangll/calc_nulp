def validate_operator(operator):
    valid_operators = ['+', '-', '*', '/', '^', '%', '√']
    if operator in valid_operators:
        return True
    else:
        print("Невірний оператор! Введіть один із (+, -, *, /, ^, %, √).")
        return False