class Coffee:
    suger = 10
    coffePowder = 20
    milk = 30
    ice = 50
    water = 30
    price = 100

    def __init__(self, coffeType, country):  # constructor for the first mixture
        self.coffeType = coffeType
        self.country = country
        Coffee.water -= 1
        Coffee.suger -= 1
        Coffee.coffePowder -= 1
    #
    # def __init__(self, coffeType, country, additionalCoffee):  # constructor for black coffee
    #     Coffee.coffePowder -= 1
    #     cLast = BlackCoffee(self.typeName, self.country,additionalCoffee)

    # def __init__(self, coffeType, country, milk, additionalCoffee, additionalMilk):  # constructor for Cappuccino
    #     Coffee.milk -= 2
    #     Coffee.coffePowder -= 1
    #     cLast = Cappuccino(self.typeName, self.country, milk, additionalCoffee, additionalMilk)
    #
    # def __init__(self, coffeType, country, milk, additionalMilk):  # constructor for Milk Coffee
    #     Coffee.milk -= 2
    #     cLast = MilkCoffee(self.typeName, self.country, milk, additionalMilk)
    #
    # def __init__(self, coffeType, country, milk, ice, additionalMilk, additionalSugur):  # constructor for Ice Coffee
    #     Coffee.milk -= 2
    #     Coffee.ice -= 1
    #     Coffee.suger -= 1
    #     cLast = IceCoffee(self.typeName, self.country, milk, ice, additionalMilk, additionalSugur)

class BlackCoffee(Coffee):
    def __init__(self, coffeType, country, additionalCoffee):
        self.coffeType = coffeType
        self.country = country
        self.additionalCoffee = additionalCoffee
        Coffee.coffePowder -= 1


class Cappuccino(Coffee):
    def __init__(self, coffeType, country, milk, additionalCoffee, additionalMilk):
        self.coffeType = coffeType
        self.country = country
        self.milk = milk
        self.additionalCoffee = additionalCoffee
        self.additionalMilk = additionalMilk
        Coffee.milk -= 2
        Coffee.coffePowder -= 1


class MilkCoffee(Coffee):
    def __init__(self, coffeType, country, milk, additionalMilk):
        self.coffeType = coffeType
        self.country = country
        self.milk = milk
        self.additionalMilk = additionalMilk
        Coffee.milk -= 2

class IceCoffee(Coffee):
    def __init__(self, coffeType, country, milk, ice, additionalMilk, additionalSugur):
        self.coffeType = coffeType
        self.country = country
        self.milk = milk
        self.ice = ice
        self.additionalMilk = additionalMilk
        self.additionalSugur = additionalSugur
        Coffee.milk -= 2
        Coffee.ice -= 1
        Coffee.suger -= 1
