class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: ${self.balance}"


if __name__ == "__main__":
    account = BankAccount("12345", "Paris", 500)

    print(account)

    account.deposit(200)
    print(account)

    account.withdraw(100)
    print(account)
    
    if __name__ == "__main__":

     account = BankAccount("12345", "Paris", 500)

    print(account)

    account.deposit(200)
    print(account)

    account.withdraw(100)
    print(account)

    try:
        account.withdraw(1000)
    except ValueError as error:
        print("Error:", error)
        
        
class SavingsAccount(BankAccount): 
    def __init__(self, account_number, owner, balance=0, interest_rate=0):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return self.balance
    
    def __str__(self):
        return (
            f"Account {self.account_number} - "
            f"Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f}, "
            f"Interest Rate: {self.interest_rate}%"
        )
        
        from bank import SavingsAccount

account = SavingsAccount("98765", "Paris", 1000, 5)

print(account)

account.deposit(500)
print(account)

account.withdraw(200)
print(account)

account.apply_interest()
print(account)