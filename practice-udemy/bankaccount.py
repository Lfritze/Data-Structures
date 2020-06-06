class Account():
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance


  def deposit(self, dep_amt):
    self.balance = self.balance + dep_amt
    print(f"Added {dep_amt} to the balance")

  def withdraw(self, wd_amt):
    if self.balance >= wd_amt:
      self.balance = self.balance - wd_amt    # or just -=wd_amt
      print("Withdraw accepted")
    else:
      print("sorry not enough cash")

  def __str__(self):
    return f"Owner is {self.owner} \nbalance is {self.balance} "


acct1 = Account('Jose',100)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(300)
print(acct1.balance)

acct1.withdraw(900)
print(acct1.balance)