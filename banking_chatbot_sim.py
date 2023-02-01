authenticated = False
on = True
balance = 0
password = input("Enter your password. You will need to remember it: ")
print("")

def security_check():
  count = 1
  global on
  global authenticated
  check = input("Enter your password: ")
  while check != password and on == True:
    if count == 3:
      print("Too many attempts. Shutting down...")
      on = False
      authenticated = False
    else:
      count += 1
      check = input("Incorrect. Try again: ")
  if check == password:
    print("Correct. Proceding...")
    print("")
    authenticated = True

def get_balance():
  security_check()
  global authenticated
  if authenticated == True:
    print("Current balance: $", balance)
    print("")

def add_to_balance():
  security_check()
  global authenticated
  if authenticated == True:
    global balance
    print("Current balance: $", balance)
    add = input("How much would you like to add to your balance? ")
    balance += int(add)
    print("New balance: $", balance)
    print("")

def change_password():
  security_check()
  global authenticated
  if authenticated == True:
    change = input("What would you like to change your password to? ")
    global password
    password = change
    print("")

def menu():
  print("(1) Change Password")
  print("(2) See Balance")
  print("(3) Add to Balance")
  print("(4) Quit")
  print("")
  choice = int(input("Where would you like to go? "))
  print("")
  if choice == 1:
    change_password()
  elif choice == 2:
    get_balance()
  elif choice == 3:
    add_to_balance()
  elif choice == 4:
    print("Closing...")
    global on
    on = False
  else:
    print("Please choose from the displayed options. ")
  print("")

while on:
  menu()
