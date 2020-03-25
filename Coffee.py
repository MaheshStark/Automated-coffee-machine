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

    def completeMadeTheCoffee(self):
        Coffee.water -= 1
        Coffee.suger -= 1
        Coffee.coffePowder -= 1


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
