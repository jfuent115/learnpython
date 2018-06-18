print ("Hello world")
x = 1
if x == 1:
	print ("x is 1")
	myfloat = 7.0
	print (myfloat)
	myint = 7
	print (myint)
	myfloat = float(7)
	print(myfloat)
	mystring = "Don't worry about apostrophes" 
	print (mystring)
	mystring = '"Isn\'t," she said.'
	print (mystring)
	print ("\"Hello\"")
	print ("First line.\nSecond line.")
	print ("""\
		Usage: thingy [OPTIONS]
		      -h      Display this usage message
		      -H hostname         Hostname to connect to
		      """)
	print (r'C:\some\name')
	hello = "hello"
	world = "world"
	helloworld = hello + " " + world
	print(helloworld)
	un = "un"
	ium = "ium"
	unununium = 3 * un + ium
	print (unununium)
	a, b = 3, 4
	print(a,b)
	py = 'Py'
	thon = 'thon'
	print ('Py' 'thon')
	text = ('Put several strings within parentheses' 'to have them joined together')
	print (text)
	cake = 'Python'
	cake[0]
	cake[-1]
	print (cake[0:2])
	print (cake[:4])
	print (cake[2:])

	pie = 'What is going on'
	myfloat = 7.6
	myint = 19

	if pie == 'What is going on':
		print ("pie: %s"  % pie)
	if isinstance(myfloat, float) and myfloat == 7.6:
		print("float: %f" % myfloat)
	if isinstance(myint, int) and myint == 19:
		print("integer: %d" % myint)

print ("Goodbye world")
