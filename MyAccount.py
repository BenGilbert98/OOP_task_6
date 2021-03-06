# Inherit Account holder class into MyAccount

# Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type),
# , balance.
from Account_holder_details import AccountHolderDetails


class MyAccount(AccountHolderDetails):
    def __init__(self, name, address, age, account_number, __pin_number):
        super().__init__(name, address, age)
        self.AccountNumber = account_number
        self.balance = 0 # Balance is set to 0 by default
        self.__pin_number = __pin_number

    # Method to deposit money to account
    def Deposit(self):
        deposit_amount = int(input("How much money would you like to deposit?     "))
        self.balance += deposit_amount
        return print(f"Your total balance is £{self.balance}")

    # Method to withdraw money to account (requires pin verification)
    def Withdrawal(self):
        test = int(input("What is your pin number?     "))
        if test == self.__pin_number:
            withdraw_amount = int(input("How much money would you like to withdraw?     "))

            if (self.balance - withdraw_amount) > 0:
                self.balance -= withdraw_amount
                return print(f"you have £{self.balance} left inside your account")
            if (self.balance - withdraw_amount) <= 0:
                overdraft_check = input("You are about to enter your overdraft would you like to continue?  (Y/N)  ")
                if overdraft_check.lower() == "y":
                    self.balance += -withdraw_amount
                    print(f"you have £{self.balance} inside your account")
                if overdraft_check.lower() == "n":
                    return print("No money has been withdrawn from your account")
            elif (self.balance - withdraw_amount) <= 0 and self.balance - withdraw_amount <= -1000:
                print("Sorry, this withdrawal will take you past your £1000 overdraft.    ")
        else:
            return

    # Function to pay bank fees
    def Bank_fees(self):
        test = int(input("What is your pin number?     "))
        if test == self.__pin_number:
            self.balance = 0.95 * self.balance
            return print(f"You have £{self.balance} left in your account")
        else:
            return
