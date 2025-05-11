import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rockpaperscissor = [rock, paper, scissors]

random_generator = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice == random_generator:
    print(rockpaperscissor[user_choice])
    print("Computer chose: ")
    print(rockpaperscissor[random_generator])
    print("It's a draw!")

if user_choice == 0:
    if random_generator == 1:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You lose!")
    elif random_generator == 2:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You win!")

elif user_choice == 1:
    if random_generator == 0:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You win!")
    elif random_generator == 2:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You lose!")

elif user_choice == 2:
    if random_generator == 0:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You lose!")
    elif random_generator == 1:
        print(rockpaperscissor[user_choice])
        print("Computer chose: ")
        print(rockpaperscissor[random_generator])
        print("You win!")

