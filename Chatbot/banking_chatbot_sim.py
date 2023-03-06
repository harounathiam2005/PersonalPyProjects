from Account import Account

on = True
accounts = []
current_user = 0

def create_account():
  acc_name = input("Enter new account name: ")
  while acc_name == "":
    print("")
    acc_name = input("Please enter a username: ")
  acc_pass = input("Enter your password. You will need to remember it: ")
  while acc_pass == "":
    print("")
    acc_name = input("Please enter a password: ")
  accounts.append(Account(acc_name, acc_pass))

def display_accounts():
  for n, i in enumerate(accounts):
    print(f"({n + 1})", "Username:", i.get_user(), "\n    Password:", i.get_pass_mutate())

def display_user_info():
  print(f"Username: {accounts[current_user].get_user()} -- Password: {accounts[current_user].get_pass_mutate()}")

# Change value of int variable passed into Account array to yield account at specific place
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

# Change status of authentication Account instance attribute
def security_check():
  count = 1
  global on
  check = input("Enter your password: ")
  while check != accounts[current_user].get_pass() and on:
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
  if accounts[current_user].get_auth():
    print("Current balance: $", accounts[current_user].get_balance())
    print("")

def add_to_balance():
  security_check()
  if accounts[current_user].get_auth():
    print("Current balance: $", accounts[current_user].get_balance())
    add = input("How much would you like to add to your balance? ")
    accounts[current_user].add_balance(int(add))
    print("New balance: $", accounts[current_user].get_balance())
    print("")

def change_password():
  security_check()
  if accounts[current_user].get_auth():
    change = input("What would you like to change your password to? ")
    accounts[current_user].set_pass(change)
    print("")

def menu():
  print("(1) Change Password")
  print("(2) See Balance")
  print("(3) Add to Balance")
  print("(4) Display Account Info")
  print("(5) Display Accounts")
  print("(6) Add Account")
  print("(7) Change Account")
  print("(8) Quit")
  print("")
  descision = input("Tell me, what would you like to do? ")
  # Utilize basic language interpreter methods of Account class
  direction = accounts[current_user].interpret(descision)
  print("")
  if direction == "1":
    change_password()
  elif direction == "2":
    get_balance()
  elif direction == "3":
    add_to_balance()
  elif direction == "4":
    display_user_info()
  elif direction == "5":
    display_accounts()
  elif direction == "6":
    create_account()
  elif direction == "7":
    switch_account()
  elif direction == "8":
    print("Closing...")
    global on
    on = False
  else:
    print("Please choose from the displayed options. ")
  print("")

create_account()
print("")

while on:
  menu()
