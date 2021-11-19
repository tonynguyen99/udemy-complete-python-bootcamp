# OOP Challenge - Create a bank account

class Account:
  def __init__(self,owner,balance=0):
    self.owner = owner
    self.balance = balance
    
  def __str__(self):
    return f'Account owner: {self.owner}\nBalance: {self.balance}'
    
  def deposit(self,depositAmount):
    if depositAmount > 0:
      self.balance += depositAmount
      print('Deposit successful!')
    else:
      print('You did not deposit anything!')
  
  def withdraw(self,withdrawAmount):
    if withdrawAmount > self.balance:
      print('You have insufficient funds!')
    else:
      self.balance -= withdrawAmount
      print('Withdrawal successful!')
  
tony = Account('Tony', 50)
print(tony)
tony.deposit(50)
print(tony)
tony.withdraw(20)
print(tony)
tony.withdraw(80)
print(tony)
tony.withdraw(1)