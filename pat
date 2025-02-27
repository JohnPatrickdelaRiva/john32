class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance 


account = BankAccount(14000)
account.deposit(5500)
account.withdraw(600)
print(account.get_balance())
