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
