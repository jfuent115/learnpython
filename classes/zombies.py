class Calc:
	def __init__(self):
		pass

	def add_list(self, x):
		answers = 0
		for num in x:
			answers += num
		return answers

	def add_lists(self, x, y):
		answers = []
		count = 0
		for num in x:
			answer = num + y[count]
			answers.append(answer)
			count += 1
		return answers
	
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
	answer = calc.add_lists([1,3,4], [1,2,7])
	print (answer)

	answer = calc.add_list([1,2,3])
	print (answer)