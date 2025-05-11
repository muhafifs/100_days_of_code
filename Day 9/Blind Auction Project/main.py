import art
import os
print(art.logo)


def highest_bidder(bid_data: dict):
    winner = ""
    for bidder in bidders_data:
        if winner == "" or bidders_data[bidder] > bidders_data[winner]:
            winner = bidder
    return winner


bidders_data = {}
while True:
    ask_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidders_data[ask_name] = bid_amount
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower().strip()
    if another_bidder == "no":
        break
    os.system('cls')

print(f"The winner is {highest_bidder(bidders_data)} with a bid of ${bidders_data[highest_bidder(bidders_data)]}")

