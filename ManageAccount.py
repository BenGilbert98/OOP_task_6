from MyAccount import MyAccount
from Account_holder_details import AccountHolderDetails


class ManageAccount(MyAccount, AccountHolderDetails):
    def __init__(self, name, address, age, account_number, pin_number):
        super().__init__(name, address, age, account_number, pin_number)
        self.balance = 0
        self.options = ["Display", "Deposit", "Withdrawal", "Pay Bank Fees"]

    def display(self):
        while True:
            method = input(f"Hello {self.name}, what would you like to do today? \n {self.options}        ")
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
