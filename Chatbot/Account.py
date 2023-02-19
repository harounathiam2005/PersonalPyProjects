class Account:

  # initialize all private objects
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.balance = 0
    self.authenticate = False

  # accessor and mutator methods essential to script function
  def add_balance(self, add):
    self.balance += add

  def get_user(self):
    return self.username

  def get_pass(self):
    return self.password

  def get_pass_mutate(self):
    pass_arr = [i for i in self.password]
    if len(pass_arr) <= 2:
      pass_arr[1] = "*"
    else:
      for i in range(1, len(pass_arr) - 1):
        pass_arr[i] = "*"
    return "".join(pass_arr)

  def get_balance(self):
    return self.balance

  def get_auth(self):
    return self.authenticate

  def set_user(self, new_user):
    self.username = new_user

  def set_pass(self, new_pass):
    self.password = new_pass

  def set_balance(self, new_balance):
    self.balance = new_balance

  def set_auth(self, new_auth):
    self.authenticate = new_auth
