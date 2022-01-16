from game_data import menu, resources

answer = ''

def check_resources_available(drink):
    return menu[drink]['ingredients']['water'] <= resources['water'] and menu[drink]['ingredients']['coffee'] <= resources['coffee'] and menu[drink]['ingredients']['milk'] <= resources['milk']

def update_resources(drink):
    resources['water'] -= menu[drink]['ingredients']['water']
    resources['coffee'] -= menu[drink]['ingredients']['coffee']
    resources['milk'] -= menu[drink]['ingredients']['milk']
    resources['money'] += menu[drink]['cost']

def get_payment(drink):
    quarters = input("How many quarters?\n")
    dimes = input("How many dimes?\n")
    nickels = input("How many nickels?\n")
    pennies = input("How many pennies?\n")

    money_inserted = float(quarters)*COINS[0] + float(dimes)*COINS[1] + float(nickels)*COINS[2] + float(pennies)*COINS[3]
    print(money_inserted)
    return round(money_inserted, 2) - menu[drink]['cost']

COINS = [0.25, 0.1, 0.05, 0.01]

while True:
    answer = input(f"What would you like? espresso/latte/capuccino\n")
    money_inserted = 0

    if answer == 'off':
        break
    elif answer == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {resources['money']}$\n")
    else:
        if check_resources_available(answer):
            money_inserted = get_payment(answer)
            if money_inserted >= 0:
                print(f"Here's {money_inserted}$ in change.\n")
                update_resources(answer)
                print(f"Here's your {answer}. Enjoy!\n")
            else:
                print(f"Sorry, not enough money. Here's the refund!\n")
        else:
            print(f"Sorry, no available resources!")