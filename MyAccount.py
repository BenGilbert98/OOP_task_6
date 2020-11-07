# Inherit Account holder class into MyAccount

# Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type),
# , balance.

from Account_holder_details import AccountHolderDetails

class MyAccount(AccountHolderDetails):
    def __init__(self, AccountNumber, Balance):
        super().__init__()
        self.AccountNumber = AccountNumber
        self.balance = Balance
        self.constructor = AccountNumber + Balance


    def Deposit(self):
        deposit_amount = int(input("How much money would you like to deposit?     "))
        self.balance += deposit_amount
        return print(f"Your total balance is £{self.balance}")

    def Withdrawal(self):
        withdraw_amount = int(input("How much money would you like to withdraw?     "))
        if self.balance - withdraw_amount >= 0:
            self.balance -= withdraw_amount
            print(f"you have £{self.balance} left inside your account")
        elif self.balance <= 0:
            overdraft_check = "You are about to enter your overdraft would you like to continue?  (Y/N)  ")
            if overdraft_check.lower == "y":
                self.balance -= withdraw_amount
                print(f"you have £{self.balance} left inside your account")
            if overdraft_check.lower in 'n':
                return print("No money has been withdrawn from your account")

    def Bankfees(self):
        self.balance *= 0.95
        return print(f"Your bank fees have been deducted. Your new balance is £{self.balance}")

    def Display(self):
        return print(self.constructor)

