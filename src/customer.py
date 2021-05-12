class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink, pub):
        if pub.check_age(self):
            amount = drink.get_price()
            self.wallet -= amount
            pub.add_money(amount)
            self.increment_drunkenness(drink)

    def increment_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
