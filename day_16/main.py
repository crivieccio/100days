from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while is_on:
    choice = input("What would you like? (espresso/latte/cappucino/): ")

    if choice.lower() == 'off':
        is_on = False
    elif choice.lower() == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if item == None:
            break
        if not coffee_machine.is_resource_sufficient(item):
            break

        money_machine.make_payment(item.cost)
        coffee_machine.make_coffee(item)
