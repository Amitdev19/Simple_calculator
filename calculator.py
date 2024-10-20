def calculator() -> None:
    """
    A simple calculator that allows the user to perform
    arithmetic operations.

    :return: None
    """
    operations = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y if y != 0 else float('nan'),
    }

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid input. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        result = operations[choice](num1, num2)

        if result != result:
            print("Error: Cannot divide by zero!")
        else:
            print(f"Result: {num1} {
                  operations[choice].__name__} {num2} = {result}")


calculator()
