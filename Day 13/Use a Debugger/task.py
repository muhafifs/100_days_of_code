import random
import maths


def mutate(a_list: list) -> None:
    """
    Takes a list of integers and prints a new list with the numbers transformed by some magic formula.
    """
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
