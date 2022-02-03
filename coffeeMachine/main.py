from random import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker=CoffeeMaker()
isON=True
menu=Menu()
money=MoneyMachine()
money.report()

print('**items in menu**')
coffeeMaker.report()

while isON:
    options = menu.get_items()
    choice=input(f"what do u want {options} ")
    if(choice=="off"):
        isON=False
    elif choice=="report":
        coffeeMaker.report()
        money.report()
    else:
        drink=menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
           coffeeMaker.make_coffee(drink)