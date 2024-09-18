def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Помилка: ділення на нуль!"
    elif operator == '^':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    elif operator == '√':
        return num1 ** 0.5
    else:
        return "Невідомий оператор"
