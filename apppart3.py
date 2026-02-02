class Wallet:
    def __init__(self):
        self.money = 0

    def add_money(self, amount):
        if amount > 0:
            self.money += amount

    def withdraw(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print("Fonduri insuficiente")

    def transfer(self, other_wallet, amount):
        if amount <= self.money:
            self.money -= amount
            other_wallet.money += amount

my_wallet = Wallet()
my_wallet.add_money(100)
my_wallet.add_money(50)

# print(my_wallet.money)


class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()

    def __str__(self):
        return f"{self.name} are {self.wallet.money} lei"

    def transfer_to(self, other_user, amount):
        self.wallet.transfer(other_user.wallet, amount)


ana = User("Ana")
mihai = User("Mihai")
dumitru = User("Dumitru")

ana.wallet.add_money(300)
mihai.wallet.add_money(150)
dumitru.wallet.add_money(500)

ana.transfer_to(mihai, 100)

dumitru.transfer_to(ana, 200)


mihai.transfer_to(dumitru, 50)


print(ana)
print(mihai)
print(dumitru)