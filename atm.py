import sys
class customer:
    """customer class with bank operation .."""
    bankname="PYTHON"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('balance after deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficient Funds..cannot perform this operation')
            sys.exit()
        self.balance=self.balance-amt
        print('balance after withdraw:',self.balance)

print('welcome to',customer.bankname)
name=input('enter your name:')
c=customer(name)
while True:
    print('d-Deposit\nw-withdraw\ne-exit')
    option=input('choose your option:')
    if option=='d' or option=='D':
       amt=float(input('enter amount:'))
       c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter amount:'))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print('THANKS FOR BANKING')
        sys.exit()
    else:
        print('invalid option ..plz choose valid option')    
