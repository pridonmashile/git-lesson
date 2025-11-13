# Simple ATM Simulation

def atm():
    print("Welcome to the Python ATM!")

    # initial balance
    balance = 1000.0  
    pin = "1234"  # preset PIN

    # user authentication
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN! Access denied.")
        return

    # main ATM menu
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == '4':
            print("Thank you for using the Python ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the ATM program
atm()