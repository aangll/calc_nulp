from calculate import calculate


def safe_calculate(num1, num2, operator):
    try:
        result = calculate(num1, num2, operator)
        return result
    except Exception as e:
        return f"Помилка: {e}"
