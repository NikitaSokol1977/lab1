while True:
    try:
        expression = input("Введите выражение (или 'выход'): ")
        if expression.lower() == 'выход':
            break
        result = eval(expression)
        print("Результат:", result)
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")