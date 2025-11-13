import random

def number_guessing_game():
    # Pick a random number from 0-10
    target_number = random.randint(0, 10)
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 0 and 10.")
    
    while True:
        try:
            # Get user input
            user_guess = int(input("Guess a number: "))
            
            # Check if the guess is within the range
            if user_guess < 0 or user_guess > 10:
                print("Please enter a number between 0 and 10.")
                continue
            
            # Check the guess
            if user_guess == target_number:
                print("Number Match! Congratulations, you guessed it!")
                break
            elif user_guess < target_number:
                print("The chosen number is too low. Try again!")
            else:
                print("The chosen number is too high. Try again!")
        
        except ValueError:
            print("Invalid input! Please enter a number.")

# Call the function
number_guessing_game()