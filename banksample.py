
class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
      self.balance+=amount

    def withdraw(self,amount):
       if self.balance-amount>=self.min_balance:
         self.balance-=amount
       else:
         print("sorry,insuff funds")

    def printstatement(self):
        print("Account Balance:",self.balance)

class current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return"{}'s current Account with Balance:{}".format(self.name,self.balance)

class savings(Account):
    def __init__(self,name,balance):                                         
         super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return"{}'s savings Account with Balance:{}".format(self.name,self.balance)

c=savings("ajay",1000)
print(c)
c.deposit(5000)
c.printstatement()
c.withdraw(16000)
c.withdraw(15000)
print(c)

c2=current('raj',2000)
c2.deposit(6000)
print(c2)
c2.withdraw(27000)
print(c2)