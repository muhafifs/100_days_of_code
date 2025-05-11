import random
from art import logo

print(logo)
print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100
''')

# using random module to choose a number between 1 and 1000
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()

# setting attempts number defending on the difficulty chosen
attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

game_over = False
while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: ").strip())

    # control flow statements to determine the position of the guess
    if guess < number:
        attempts -= 1
        print(f"Too low\nGuess Again")
    elif guess > number:
        print(f"Too high\nGuess Again")
        attempts -= 1
    else:
        # guess = number so the player wins
        print(f"You got it!. The answer was {number}")
        game_over = True

    # end the game if the player runs out of attempts
    if attempts == 0:
        print(f"You've run out of guesses. The number was {number}")
        game_over = True
