print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y":
    bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
