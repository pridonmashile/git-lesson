# Simple Calculator with Error Handling

try:
    # Step 1: Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Step 2: Display operator choices
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Step 3: Get user choice
    choice = input("Enter your choice (+, -, *, /): ")

    # Step 4: Perform calculation based on choice
    if choice == '+':
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == '-':
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == '*':
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == '/':
        # Error handling for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    else:
        print("Invalid operator selected.")

# Step 5: Handle non-numeric input
except ValueError:
    print("Error: Please enter valid numbers only.")