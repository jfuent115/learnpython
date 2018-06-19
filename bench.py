cakes = 'My friends names are {1} and {0}'
cake = 'My name is {1}{2}{0}'
first = 'bill'
last = 'jones'
middle = 'josh'
my_name = 'my name is {first} {1} {0} '
print (cake.format(first[0], middle[0], last[0]))
print (cakes.format("tom", "bob"))
print (my_name.format('fuentes', 'bill', first='josh'))