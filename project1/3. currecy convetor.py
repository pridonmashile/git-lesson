def show_menu():
    print("\n--- Currency Converter ---")
    print("1. USD to ZAR")
    print("2. ZAR to USD")
    print("3. USD to EUR")
    print("4. EUR to USD")
    print("5. Exit")

def convert(amount, rate):
    return amount * rate

def main():
    USD_TO_ZAR = 18.20
    ZAR_TO_USD = 1 / USD_TO_ZAR
    USD_TO_EUR = 0.92
    EUR_TO_USD = 1 / USD_TO_EUR

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount in USD: "))
            print(f"{amount} USD = {convert(amount, USD_TO_ZAR):.2f} ZAR")

        elif choice == "2":
            amount = float(input("Enter amount in ZAR: "))
            print(f"{amount} ZAR = {convert(amount, ZAR_TO_USD):.2f} USD")

        elif choice == "3":
            amount = float(input("Enter amount in USD: "))
            print(f"{amount} USD = {convert(amount, USD_TO_EUR):.2f} EUR")

        elif choice == "4":
            amount = float(input("Enter amount in EUR: "))
            print(f"{amount} EUR = {convert(amount, EUR_TO_USD):.2f} USD")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()