import random
import sys
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_generator(collection: list, amount=1):
    """
    this function is used to generate the cards that will be dealt to the player and computer.
    """
    draw_card = random.choice(cards)
    return collection.append(draw_card)

def is_winner(player: int, computer: int):
    """
    this function is made to decide who's the winner.
    """
    global player_score
    global computer_score

    if computer_score < 17:
        card_generator(computer_cards)
        computer_score = sum(player_cards)
        is_winner(player_score, computer_score)
    elif computer > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
        computer_score = sum(computer_cards)

    if player > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        player_score = sum(player_cards)
    else:
        player_score = sum(player_cards)

    if player_score > 21:
        a = "You went over. You lose :("
        return a
    elif player_score > computer_score:
        b = "Congrats, You win!"
        return b
    elif player_score < computer_score:
        if computer_score > 21:
            b = "Congrats, You win!"
            return b
        else:
            c = "Sorry, you lose"
            return c
    else:
        draw = "It's a draw"
        return draw

game_over = False
while not game_over:
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip()
    if play == "y":
        print("" * 50)
        for _ in range(2):
            card_generator(player_cards)
            card_generator(computer_cards)
    else:
        sys.exit("Bye!")

    print(logo)

    player_score += sum(player_cards)
    computer_score += sum(computer_cards)

    print(f"Your cards: {player_cards} current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if player_score == 21:
        print("It,s a Blackjack. You win! ")
        continue

    add_card = False
    while not add_card:
        add = input("Type 'y' to get another card, type 'n' to pass ").strip()

        if add == "y":
            card_generator(player_cards)
            winner = is_winner(player_score, computer_score)
            if player_score > 21:
                print(f"Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You went over. You lose :(")
                add_card = True
            else:
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                continue

        elif add == "n":
            winner = is_winner(player_score, computer_score)
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(winner)

            add_card = True
