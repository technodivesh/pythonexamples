# class / Inheritance

class BankAccount():
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposite(self,amount):
		self.balance += amount
		return self.balance

class MinimumBalanceAccount(BankAccount):

	def __init__(self,min_bal):
		BankAccount.__init__(self)  
		self.min_bal = min_bal

	def withdraw(self,amount):
		
		if (self.balance - amount) < self.min_bal:
			return "Sorry, minimum balance must be maintained."

		self.balance -= amount
		return self.balance


