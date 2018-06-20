class BasicOperators:
	def __init__(self):
		pass

	def combine_list(self, x, y):
		return x + y

	def count_list(self, l):
		return len(l)

if __name__ == '__main__':
	bo = BasicOperators()

	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

	combine_list = bo.combine_list(x, y)
	count_list = bo.count_list(combine_list)

	print (combine_list)
	print (count_list)

	x = [1, 2, 3, 4, 5, 6]
	y = [11, 12, 13, 14, 15, 16]

	combine_list = bo.combine_list(x, y)
	count_list = bo.count_list(combine_list)

	print (combine_list)
	print (count_list)