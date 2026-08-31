class BankAccount:
    def __init__(self, owner : str, balance : float=100):
        self.owner = owner
        self.balance = balance
    def deposit(self,add):
        if add < 0:
            print("You cannot deposit negative numbers")
            return
        self.balance += add
        print(f"{self.owner} deposited {add} ")
    def withdraw(self,exit):

            if exit > self.balance:
                print("You cannot withdraw more money")
                return False
            elif exit<0:
                print("You cannot withdraw negative numbers")
                return False
            else:
                self.balance -= exit
                print("withdraw successful ")
                return True

    def show_balance(self):
        print(f" dear {self.owner}  your balance is {self.balance}")
user_name=input("Enter your fulname: ")
account=BankAccount(user_name)
while True:

    print("1. deposit")
    print("2. withdraw")
    print("3. show_balance")
    print("4. Exit")
    print("chose 1-4")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter number between 1-4")
        continue

    if choice==1:
        try:
            deposit_amount=float(input("Enter your deposit amount: "))
            account.deposit(deposit_amount)
        except ValueError:
            print("Please enter a numeric value")
    elif choice==2:
        try:
            withdraw_amount=float(input("Enter your withdraw amount: "))
            account.withdraw(withdraw_amount)
        except ValueError:
            print("Please enter a numeric value")

    elif choice==3:
        account.show_balance()
    elif choice==4:
        print("exit yout account")
        break
    else:
        print("Please enter number between 1-4")














