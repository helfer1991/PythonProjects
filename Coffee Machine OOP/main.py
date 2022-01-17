from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True: 
    answer = input(f"Which of the following drinks do you wish? {menu.get_items()}\n")

    if answer == 'off':
        break
    elif answer == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif menu.find_drink(answer) != None:
        drink = menu.find_drink(answer)
        print('The drink you chose is available')
        if coffeeMaker.is_resource_sufficient(drink):
            moneyMachine.make_payment(drink.cost)
            coffeeMaker.make_coffee(drink)


