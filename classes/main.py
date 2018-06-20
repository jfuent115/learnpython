class Printer:
	def __init__(self, name):
		self.name = name4

	def print_add(self, num):
		tmpl = 'My answer is {} and my name is {}'
		print (tmpl.format(num, self.name))
		return

class Calc:
	def __init__(self):
		self.printer = Printer('Josh')

	def add_times(self, x, y):
		num = self.add(x, y) + self.times(x, y)
		self.printer.print_add(num)
		return 

	def add(self, x, y):
		return x + y

	def times(self, x, y):
		return x * y

	def divide(self, x, y):
		return x / y

	def minus(self, x, y):
		return x - y

if __name__ == '__main__':
	calc = Calc()
	printer = Printer('Josh')

	calc.add_times(1, 2)
	printer.print_add(12)