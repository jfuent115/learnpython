dataset = [
	('John', 'Doe', 53.63),
	('Bob', 'James', 43.66),
	('Bob', 'James', 43.66),
	('Bob', 'James', 43.66),
	('Bob', 'James', 43.66)
]

msg_tmpl = 'Hello {} {}. Your current balance is ${}.'

for brown_bear in dataset:
	msg = msg_tmpl.format(*brown_bear)
	print (msg)