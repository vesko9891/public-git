def calculator():
    print("Избери операция:")
    print("1. Събиране")
    print("2. Изваждане")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Въведи номер на операция (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Въведи първото число: "))
            num2 = float(input("Въведи второто число: "))
        except ValueError:
            print("Моля, въведи валидно число.")
            return

        if choice == '1':
            print("Резултат:", num1 + num2)
        elif choice == '2':
            print("Резултат:", num1 - num2)
        elif choice == '3':
            print("Резултат:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Резултат:", num1 / num2)
            else:
                print("Деление на нула не е позволено.")
    else:
        print("Невалиден избор.")

calculator()
