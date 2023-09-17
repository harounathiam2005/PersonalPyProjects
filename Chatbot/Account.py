class Account:
  
  # initialize all private objects
  def __init__(self, username, password, balance=None):
    self.username = username
    self.password = password
    self.balance = 0
    self.authenticate = False
    self.request_vars = [["change", "password", 2], ["see", "show", "balance", 2], ["add", "balance", 2], ["display", "show", "account", "info", 3], ["display", "show", "accounts", 2], ["add", "account", 2], ["change", "account", 2], ["quit", "exit", "leave", 1]]
    self.current_input = ""
    confidence = 0
    threshold = 2
    self.threshold = threshold
    self.confidence = confidence

  # accessor and mutator methods
  def add_balance(self, add):
    self.balance += add

  def get_user(self):
    return self.username

  def get_pass(self):
    return self.password

  def get_pass_mutate(self):
    return self.password[0] + self.password[1:len(self.password) - 2] + self.password[len(self.password) - 1]

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

  def set_current_input(self, new_ans):
    self.current_input = new_ans

  def debug(self):
    print(self.interpret)
    print(self.current_input)

  def interpret(self, word):
    words = word.lower().split()
    confidence = 0
    for list in self.request_vars:
      threshold = list[len(list) - 1]
      for i in list:
        if i in words:
          confidence += 1
          if confidence >= threshold:
            value = self.request_vars.index(list) + 1
            return str(value)
