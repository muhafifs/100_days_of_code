import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

continues = True

while continues:
    print(art.logo)
    print("Welcome to Calculator made by siro????")

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
