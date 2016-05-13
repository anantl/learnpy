#Beginning of the chapter that teaches control flow statements in python

number = 42

correct = False

while (correct == False):
	ans = int(input("Please enter the answer to life and the universe: "))
	if ans == number:
		print ("Oh mighty hitchhiker! I welcome thee")
		print ("This is a very drab place though")
		correct = True
	elif ans > number:
		print ("You are telling way more than what was asked of you")
	else:
		print("You under estimate us fool!")

print ("Go away now!")
