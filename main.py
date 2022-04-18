import menu
from menu import MENU, resources


def checking_resources(order_ingredients):
    """return true when order can be made """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there's no enough {item}")
            return False
    return True


def payment():
    """Returns the total coins paid by the customer"""
    print("Please insert your coins")
    total = float(input("How many quarters?!\n")) * 0.25
    total += float(input("How many dimes?!\n")) * 0.10
    total += float(input("How many nickles?!\n")) * 0.10
    total += float(input("How many pennies?!\n")) * 0.01
    return total


def is_payment_ok(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        menu.profit += cost
        print(f"Please Take your change {change} Dollars")
        return True

    else:
        print("Money isn't enough")
        return False


def make_drink(drink_name, order_ingredients):
    """reduce the ingredients from resources + Printing Coffee is ready """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {drink_name} ☕ is ready")


is_on = True
while is_on:
    start = input("What would you like? (espresso/latte/cappuccino):")
    if start == "off":
        print("Machine has been trued off")
        is_on = False
    elif start == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money = {menu.profit}")
        # is_on = False
    else:
        drink = MENU[start]
        if checking_resources(drink["ingredients"]):
            payment = payment()
            if is_payment_ok(payment, drink["cost"]):
                make_drink(start, drink["ingredients"])
            # is_on = False
