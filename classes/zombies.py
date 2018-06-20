class Calc:
	def __init__(self):
		pass
	
	def add(self, x, y):
		return x + y
	
	def times(self, x, y):
		return x * y
	
	def minus(self, x, y):
		return x - y
	
	def divide(self, x, y):
		return x / y

if __name__ == '__main__':
	calc = Calc()
	print (calc.add(1, 2))