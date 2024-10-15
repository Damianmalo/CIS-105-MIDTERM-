import random

def guessing_game():
    secret_number = random.randint(1, 50)  
    guess = None  
    
    print("Welcome to the guessing game!")
    print("I have selected a number between 1 and 50.")
    
    
    while guess != secret_number:
        guess = int(input("Enter your guess: "))  
        
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Guess again.")
        else:
            print("Congratulations! You guessed the number!")


guessing_game()
