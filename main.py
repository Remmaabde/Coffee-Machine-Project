MENU = {
    "espresso" : {
        "ingridients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "latte" :{
        "ingredients" : {
             "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappucino" : {
        "ingredients" : {
            "water" : 250,
            "milk": 100,
            "coffe" : 24,
        },
        "cost" : 3.0,
    }
}
profit = 0
resources = {
    "water" : 300,
    "milk" :200,
    "coffee" :100,
}

def is_resource_sufficient(order_ingredients):
    '''Returns true when orders can be made and False when it's Sufficient'''
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry There is no enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    '''Returns the total calculated from the coins inserted'''
    print("Please insert coins.")
    total = int(input(" How many quarters?: ")) * 0.25
    total += int(input(" How many dimes?: ")) * 0.1
    total += int(input(" How many nickles?: ")) * 0.05
    total += int(input(" How many pennies?: ")) * 0.01
    return total

def is_transaction_successfull(money_recieved,drink_cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost

        return True
    else:
        print("Sorry, That's not enough money. Money Refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy")





is_on = True

while is_on:
    choice = input("What would you like? (Espresso / Latte / Cappucino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water {resources['water']}ml")
        print(f"milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"money ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successfull(payment,drink["cost"])
