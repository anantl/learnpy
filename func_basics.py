import average_marks.py

def max_calc(a=2, b=1):
	if (a > b):
		print("A is greater")
	elif (b > a):
		print("B is greater")
	else:
		print("Both the values are equal")

max_calc(10,100)
x = 10
y = 11
print("The values passed are {} and {}".format(x, y))

max_calc(x,y)
max_calc()
average_marks
