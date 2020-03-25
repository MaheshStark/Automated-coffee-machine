from filecmp import cmp

import Coffee

moneyInput = 0
sugur = 1
milk = 1
ice = 1
coffeePowder = 1
completeBusiness = False
print("|---------------------------------------------------------------------|")
print("|Coffee types---------->>>                                            |")
print("|    - 1.Black coffee                     2.Cappuccino                |")
print("|    - 3.Milk Coffee                      4.Ice Coffee                |")
print("|                                                          100 Rs each|")
print("|---------------------------------------------------------------------|")

print("|---------------------------------------------------------------------|")
print("|Available ingrediens---------->>>                                    |")
print("|    - 1.coffee -" + str(Coffee.Coffee.coffePowder) + "                    2.Milk -" + str(
    Coffee.Coffee.milk) + "                     |")
print("|    - 3.ice    -" + str(Coffee.Coffee.ice) + "                    4.water-" + str(
    Coffee.Coffee.water) + "                     |")
print("|    - 3.sugur  -" + str(Coffee.Coffee.suger) + "                                                   |")
print("|---------------------------------------------------------------------|")

while completeBusiness==False:
    typeCoffee = int(input('What is the coffee type you want: '))
    if typeCoffee == 1:
        typeName = "Black coffee"
    elif typeCoffee == 2:
        typeName = "Cappuccino"
    elif typeCoffee == 3:
        typeName = "Milk Coffee"
    elif typeCoffee == 4:
        typeName = "Ice Coffee"

    country = input('Which country made coffee you want: ')

    while Coffee.Coffee.price > moneyInput:
        money = input('Add the enough Money: ')
        moneyInput += int(money)
        if moneyInput > Coffee.Coffee.price:
            returnMoney = moneyInput - Coffee.Coffee.price
            print('Take your return Money:' + str(returnMoney) + 'Rs')
    # makeCoffee()

    #
    # def makeCoffee():  # mack a coffee method
    if typeName == "Cappuccino":
        ingredient = 1
        c1 = Coffee.Cappuccino(typeName, country, milk, coffeePowder, milk)
        c1.completeMadeTheCoffee()
    elif typeName == "Black coffee":
        c1 = Coffee.BlackCoffee(typeName, country, coffeePowder)
        c1.completeMadeTheCoffee()
    elif typeName == "Milk Coffee":
        c1 = Coffee.MilkCoffee(typeName, country, milk, milk)
        c1.completeMadeTheCoffee()
    elif typeName == "Ice Coffee":
        c1 = Coffee.IceCoffee(typeName, country, milk, ice, milk, sugur)
        c1.completeMadeTheCoffee()

    print("Take your coffee from the dispathch")
    print("Coffee type : " + c1.coffeType)
    print("Country     : " + c1.country)

    print("|---------------------------------------------------------------------|")
    print("|Available ingrediens---------->>>                                    |")
    print("|    - 1.coffee -" + str(Coffee.Coffee.coffePowder) + "                    2.Milk -" + str(
        Coffee.Coffee.milk) + "                     |")
    print("|    - 3.ice    -" + str(Coffee.Coffee.ice) + "                    4.water-" + str(
        Coffee.Coffee.water) + "                     |")
    print("|    - 3.sugur  -" + str(Coffee.Coffee.suger) + "                                                   |")
    print("|---------------------------------------------------------------------|")
    moneyInput = 0
    print("Do you want to Shopping more?")
    print("1. yes          2. No")
    comp = int(input('Input your openion: '))
    if comp == 2:
        completeBusiness = True
print("Thank you come again!!!!!!")