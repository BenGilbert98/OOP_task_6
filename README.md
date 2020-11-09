Create an AccountHolderDetails class with attributes name, address, age, 

Inherit Account holder class into MyAccount

Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type),
, balance.

Create a constructor () with parameters: accountNumber,  balance.

Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.

Create manageAccount class and import everything from BankAccount class
call all methods in manageAccount class that have are available from parent class

Create a display() method to display account details.

## Create a README.md for your documentation of this task.

### Main file
```
from Account_holder_details import AccountHolderDetails
from ManageAccount import ManageAccount
from MyAccount import MyAccount

# Prompts the user for inputs
name = input("What is your name?    ")
address = input("What is your address?    ")
age = int(input("What is your age?    "))
account_number = int(input("What is your account number?    "))
__pin_number = int(input("What is your pin number?    "))

account_holder_details = AccountHolderDetails(name, address, age)
my_account = MyAccount(name, address, age, account_number, __pin_number)
manage_account = ManageAccount(name, address, age, account_number, __pin_number)


manage_account.display()
```
- In this file we import the classes from other files in order to use them
- The user is then prompted in order to gain information about them
- pin number is hidden as it is very important to keep protected
- The display function is then called from Manage Account which runs the programs.

## Account_Holder_Details
```
class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
```
- This class is responsible for storing the account holder details

## MyAccount
```
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

```
- The code below is responsible for setting a baseline balance for the account
```  
def __init__(self, name, address, age, account_number, __pin_number):
        super().__init__(name, address, age)
        self.AccountNumber = account_number
        self.balance = 0 # Balance is set to 0 by default
        self.__pin_number = __pin_number
```
- The methods below are responsible for changing the balance of the account as well as making checks when withdrawing money. Similarly, if the user is about to go into an overdraft they are warned.
```
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
```
## Manage Account
- This class is responsible for running the methods within MyAccount class through inputs from the user.
```
from MyAccount import MyAccount
from Account_holder_details import AccountHolderDetails


class ManageAccount(MyAccount, AccountHolderDetails):
    def __init__(self, name, address, age, account_number, pin_number):
        super().__init__(name, address, age, account_number, pin_number)
        self.balance = 0
        self.options = ["Display", "Deposit", "Withdrawal", "Pay Bank Fees"]

    # Function to display information and take user promt to determine what action to take
    def display(self):
        while True:
            method = input(f"Hello {self.name}, what would you like to do today? \n {self.options} \n type exit to "
                           f"leave       ")
            if method.lower() == "display":
                print(f"Hello {self.name}, your current balance is £{self.balance}")

            if method.lower() == "deposit":
                self.Deposit()

            if method.lower() == "withdrawal":
                self.Withdrawal()

            if method.lower() == "pay bank fees":
                self.Bank_fees()

            elif method.lower() == "exit":
                break

```