class BankAccount:
def __init__(self, account_number, owner, balance=0):
self.account_number = account_number
self.owner = owner
self.balance = balance
def deposit(self, amount):
raise ValueError("Insufficient funds.")
def __str__(self):
account = BankAccount("12345", "Paris", 500)
account.deposit(200)
account.withdraw(100)
account.withdraw(1000)
try:
    account.withdraw(1000)

except ValueError as e:
    print(e)
    