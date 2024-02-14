from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
moneymachine = MoneyMachine()

identity = input("Are you a customer or an employee? ").lower()

# Taking order and making coffee #
if identity == "customer":
    menu_items = menu.get_items()

    print("We offer 3 kinds of coffee\n")
    print(f"{menu_items}\n")

    order_name = input("What would you like? ")
    drink = menu.find_drink(order_name = order_name)

    can_make = coffee_machine.is_resource_sufficient(drink= drink)
    if not can_make:
        print("Please turn to an employee for a refill.")
        quit()

    payment_successful = moneymachine.make_payment(cost = drink.cost)
    if not payment_successful:
        print("Sorry, I think you did not insert money.")
        quit()

    coffee_machine.make_coffee(order= drink)

elif identity == "employee":
    moneymachine.report()
    print("\n")
    coffee_machine.report()
    print("\n")
    refill = input("Would you like to refill? Yes/No ").lower()

    if refill != "yes":
        pass
    else:
        coffee_machine.refill()


