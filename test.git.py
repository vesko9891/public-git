def calculator():
    print("Добре дошъл в Калкулатора!")
    print("Операции: +  -  *  /")
    
    try:
        num1 = float(input("Въведи първо число: "))
        operation = input("Избери операция (+, -, *, /): ")
        num2 = float(input("Въведи второ число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Грешка: Деление на нула!")
                return
        else:
            print("Невалидна операция.")
            return

        print(f"Резултат: {result}")

    except ValueError:
        print("Моля, въведи валидни числа!")

calculator()

