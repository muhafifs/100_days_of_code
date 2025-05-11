
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

continues = True

while continues:
    print(logo)
    print("Welcome to Calculator made by siro")

    try:
        number_one = float(input("What's the first number?: ").strip())
    except ValueError:
        print("That's not a valid number")
        continue

    print(operation.keys())

    old_calc = True
    while old_calc:
        operator = input("Pick an operation: ").strip()

        try:
            number_two = float(input("What's the second number?: ").strip())
        except ValueError:
            print("That's not a valid number")
            continue

        result = operation[operator](number_one, number_two)
        print(f"{number_one} {operator} {number_two} = {result}")

        play_again = input(f"Type 'yes' to continue calculating with {operation[operator](number_one, number_two)} /"
                           f"or 'no' to start a new calculation \n").lower()

        if play_again == "yes":
            number_one = result
        else:
            print("\n" * 50)
            old_calc = False
