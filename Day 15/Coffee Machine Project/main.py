import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

coin = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}
# TODO 1: Ask for user input about coffee choice
operate = False
while not operate:
    order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    # Turning off machine with command from maintainer
    if order == "off":
        sys.exit("Turning off")
    elif order == "report":
        # printing resources but adjusting for
        for resource in resources:
            if resource == "Water" or resource == "Milk":
                print(f"{resource}: {resources[resource]}ml")
            elif resource == "Coffee":
                print(f"{resource}: {resources[resource]}g")
            else:
                print(f"{resource}: ${resources[resource]}")

    if order == "report":
        continue

    for check_resource in MENU:
        if


