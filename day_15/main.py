from collections import namedtuple

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}


def beverage_prompt():
    return input("What would you like? (espresso/latte/cappuccino):")


def report():
    for k, v in resources:
        if k.lower() == 'coffee':
            print(f'{k.capitalize()}: {v}g')
        elif k.lower() == 'money':
            print(f'{k.capitalize()}: ${v}')
        print(f'{k.capitalize()}: {v}ml')


def check_resources(choice):
    ingredients = MENU[choice]['ingredients']
    Result = namedtuple('Result', ['have_enough', 'resource'])
    for k in ingredients:
        if resources[k] < ingredients[k]:
            return Result(have_enough=False, resource=k)
    return Result(have_enough=True, resource='')


def process_coins():
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    return quarters * coins["quarter"] + dimes * coins["dime"] + nickels * coins["nickel"] + pennies * coins["penny"]


def inserted_enough_money(money, cost):
    if cost > money:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    elif money == cost:
        update_money(cost)
        return True
    else:
        update_money(cost)
        change = money - cost
        print(f'Here is {change} dollars in change.')
        return True


def update_money(money):
    if 'money' in resources:
        resources['money'] += money
    else:
        resources['money'] = money


def make_coffee(choice):
    ingredients = MENU[choice]['ingredients']
    for k, v in ingredients.items():
        resources[k] -= v
    print(f'Here is your {choice}. Enjoy!')


def main():
    choice = ''
    while choice.lower() != "off":
        choice = beverage_prompt()
        if choice.lower() == 'report':
            report()
            break

        result = check_resources(choice=choice)
        if not result.have_enough:
            print(f'Sorry there is not enough {result.resource}')
            break

        money = process_coins()
        if inserted_enough_money(money, MENU[choice]['cost']):
            make_coffee(choice)


if __name__ == "__main__":
    main()
