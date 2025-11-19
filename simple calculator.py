# Simple Calculator in Python

print("--- Python Calculator ---")

try:
    # 1. Get user input
    # We use float() so we can handle decimals like 5.5
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # 2. Check the operator and calculate
    if op == '+':
        result = num1 + num2
        print(f"Result: {result}")

    elif op == '-':
        result = num1 - num2
        print(f"Result: {result}")

    elif op == '*':
        result = num1 * num2
        print(f"Result: {result}")

    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {result}")

    else:
        print("Error: Invalid operator!")

except ValueError:
    print("Error: You entered text instead of a number.")

# 3. Keep window open (prevents it from closing instantly if you double-click the file)
input("\nPress Enter to exit...")