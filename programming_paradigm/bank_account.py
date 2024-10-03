class BankAccount:
    def __init__(self,initial_val=0):
        self.account_balance=initial_val
     
    def deposit(self,amount):
        self.account_balance+=amount
    
    def withdraw(self,amount):
        if amount>self.account_balance:
            return False
        self.account_balance-=amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
