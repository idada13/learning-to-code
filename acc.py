class Account:

    def __init__(self, filepath):
        self.filepaths=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, monies):
        self.balance=self.balance + monies

    def commit(self): # to save changes to the balance
        with open(self.filepaths, 'w') as file:
            file.write(str(self.balance))

class Savings(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

savings=Savings("balance.txt",1) # 1 is the fee amount
savings.transfer(100)
print(savings.balance)
savings.commit()

#    account=Account("balance.txt")
#    print(account.balance)
#    account.deposit(500)
#    print(account.balance)
#    account.commit()
