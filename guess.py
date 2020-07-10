# NUMBER GUESSING GAME
print('Number guessing game')

# Variable to store the secret number
secret_number = 12

# Variable to assume the number of guesses 
guess_count = 0

# Variable to store maximum number of guesses
guess_limit = 3

# While loop to repeatedly ask a user to make a guess
while guess_count < guess_limit:
    # Get user input and store in a variable
    # The int function converts user input i.e string to an integer 
    guess = int(input('Guess a number between 1 and 15: ')) 

    # Increment guess_count by one for each guess made by user
    guess_count += 1

    # Checking to see if the user made the right guess
    if guess == secret_number:
        print("You've won! You made the right guess")
        break

    elif guess < secret_number:
        print(f"Your guess is too low! Guess a number higher than {guess}")
    
    elif guess > secret_number:
        print(f"Your guess is high! Guess a number lower than {guess}")

else:
    print("You've lost! Try again.")
