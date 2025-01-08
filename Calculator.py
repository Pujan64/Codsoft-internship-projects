def calculator():
    try:
        num1 = float(input("Enter the first number: "))  # Allow decimal input
        num2 = float(input("Enter the second number: "))  # Allow decimal input
        operation = input("Enter the operation (+, -, *, /): ").strip()

        if operation == '+':
            print(f"Result: {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the calculator function only once
calculator()
