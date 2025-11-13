def login_system():
    # Declare the password and username
    username = "pridon"
    password = "12345"

    # Initialize attempt counter
    attempts = 0

    while attempts < 3:
        # Get user input
        user_input_username = input("Enter your username: ")
        user_input_password = input("Enter your password: ")

        # Check credentials
        if user_input_username == username and user_input_password == password:
            print("Login successful!")
            return
        else:
            attempts += 1
            print(f"Incorrect username or password. Attempts remaining: {3 - attempts}")

    # If attempts exceed 3, lock the account
    print("Maximum attempts exceeded. Account locked.")

# Call the function
login_system()