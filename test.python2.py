def calculator():
    print("=== Добре дошъл в Python Калкулатора ===")

    while True:
        print("\nИзбери операция:")
        print("1. Събиране (+)")
        print("2. Изваждане (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Изход (x)")

        choice = input("Въведи номер или символ на операция: ").strip()

        if choice.lower() in ['5', 'x', 'exit', 'изход']:
            print("Благодаря, че използва нашия калкулатор. Довиждане!")
            break

        if choice not in ['1', '2', '3', '4', '+', '-', '*', '/']:
            print("Невалиден избор. Опитай отново.")
            continue

        try:
            num1 = float(input("Въведи първо число: "))
            num2 = float(input("Въведи второ число: "))
        except ValueError:
            print("Грешка: Моля, въведи валидни числа.")
            continue

        if choice in ['1', '+']:
            result = num1 + num2
            op = '+'
        elif choice in ['2', '-']:
            result = num1 - num2
            op = '-'
        elif choice in ['3', '*']:
            result = num1 * num2
            op = '*'
        elif choice in ['5', '/']:
            if num2 == 0:
                print("Грешка: Деление на нула не е позволено.")
                continue
            result = num1 / num2
            op = '/'

        print(f"\n➡️  {num1} {op} {num2} = {round(result, 2)}")

# Стартиране на калкулатора with change
calculator()

