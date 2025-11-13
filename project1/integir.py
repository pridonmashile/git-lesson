def check_even_odd():
    while True:
        try:
            # Get user input
            num = int(input("Enter an integer: "))
            
            # Check if the number is even or odd
            if num % 2 == 0:
                print(f"{num} is an even number.")
            else:
                print(f"{num} is an odd number.")
        
        except ValueError:
            print("Invalid input! Please enter an integer.")
        
        # Ask user if they want to continue
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            break

# Call the function
check_even_odd()