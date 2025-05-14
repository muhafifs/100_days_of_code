import sys 
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if choice == "off":
        sys.exit("Turning off ...")
    elif choice == "report":
        machine.report()
        money.report()
        continue
    else:
        order = menu.find_drink(choice)
        if not menu.find_drink(choice):
            continue    

    if machine.is_resource_sufficient(menu.find_drink(choice)):
        if money.make_payment(order.cost):
            machine.make_coffee(menu.find_drink(choice))
        else:
            continue
        
