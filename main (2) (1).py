'''Implement a class called Bank Account that represents a Bank account.The class should have private
 attributes for account number,account holder name ,ans account balance.Include methods to
  deposit money, withdraw money,and display the account balance
  cannot be accessed directly from outside the class-write a program to create an instance of the
  Bank Account class and test the deposit and withdrawel
  functionality'''

class BackAccount:

  def __init__(self,account_number,account_holder_name,initial _balance=0.0):
                                self.__account_number= account_number
  self.__account_holder_name= account_holder_name
  self.__account_balance=initial_balance

def deplosit ( self,amount):
  if amount>0:
     self.__account_balance +=amount
    #self.__account_balance=self.__account_balance+amount
 print("Deposited ₹{}.New balance:₹{}".format(amount,
                              self.__account_balance))
else:
print ("ENvalid deposit amount.")

def withdraw (self,amount):
if amount >0and amount<=self.__account _balance:
self.__account_balance_=amount 
# self.__account_balance=self.__account_balance_amount 
print ("withdraw ₹{}.new balance: ₹{}".format (amount,
self.__account_balance))
else:
print("Invalid withdrawel amount or insufficient balance.")

def display_balancefor(self):
  print ("Account#{}):₹{}".format self.__account_holder_name
self.__accont_number,self.__ account _balance) )



#create an instance  of the Bank Account  class
account =BankAccount(account_number="123456789",)
account_holder_name="hari prabu",
initial_balance=5000.0)

# test deposit ans withdrawal  functionality
account.display.Balance()
# account.deposit(500.0)
account.withdraw (200.0)
account.withdraw (20000.0)
account.display_balance()