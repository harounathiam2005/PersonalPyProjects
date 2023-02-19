from Account import Account

on = True
username = input("Enter your username: ")
password = input("Enter your password. You will need to remember it: ")
accounts = [Account(username, password)]
current_user = 0
print("")

def create_account():
  acc_name = input("Enter new account name: ")
  acc_pass = input("Enter your password. You will need to remember it: ")
  accounts.append(Account(acc_name, acc_pass))

def display_accounts():
  for n, i in enumerate(accounts):
    print(f"({n + 1})", "Username:", i.get_user(), "\n    Password:", i.get_pass_mutate())

def display_user_info():
  print(f"Username: {accounts[current_user].get_user()} -- Password: {accounts[current_user].get_pass_mutate()}")

def switch_account():
  display_accounts()
  print("")
  choice = input("Choose an account to switch to: ")
  decision = False
  while decision == False:
    if int(choice) in range(1, len(accounts) + 1):
      global current_user
      current_user = int(choice) - 1
      print("")
      print("Switching accounts...")
      decision = True
    else:
      print("")
      choice = input("Please choose from the displayed options. ")

def security_check():
  count = 1
  global on
  check = input("Enter your password: ")
  while check != accounts[current_user].get_pass() and on == True:
    if count == 3:
      print("Too many attempts. Shutting down...")
      on = False
      accounts[current_user].set_auth(False)
    else:
      count += 1
      check = input("Incorrect. Try again: ")
  if check == accounts[current_user].get_pass():
    print("Correct. Proceding...")
    print("")
    accounts[current_user].set_auth(True)

def get_balance():
  security_check()
  if accounts[current_user].get_auth() == True:
    print("Current balance: $", accounts[current_user].get_balance())
    print("")

def add_to_balance():
  security_check()
  if accounts[current_user].get_auth() == True:
    print("Current balance: $", accounts[current_user].get_balance())
    add = input("How much would you like to add to your balance? ")
    accounts[current_user].add_balance(int(add))
    print("New balance: $", accounts[current_user].get_balance())
    print("")

def change_password():
  security_check()
  if accounts[current_user].get_auth() == True:
    change = input("What would you like to change your password to? ")
    accounts[current_user].set_pass(change)
    print("")

def menu():
  print("(1) Change Password")
  print("(2) See Balance")
  print("(3) Add to Balance")
  print("(4) Display Current Account Info")
  print("(5) Display Accounts")
  print("(6) Add Account")
  print("(7) Change Account")
  print("(8) Quit")
  print("")
  choice = input("Where would you like to go? ")
  print("")
  if choice == "1":
    change_password()
  elif choice == "2":
    get_balance()
  elif choice == "3":
    add_to_balance()
  elif choice == "4":
    display_user_info()
  elif choice == "5":
    display_accounts()
  elif choice == "6":
    create_account()
  elif choice == "7":
    switch_account()
  elif choice == "8":
    print("Closing...")
    global on
    on = False
  else:
    print("Please choose from the displayed options. ")
  print("")

while on:
  menu()
