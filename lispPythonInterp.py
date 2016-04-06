
# #convert a string into a lits of charecters
# def tokenize(string):
# 	return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def evaluator(expression):
	numbers = []
	for letter in expression:
		if letter.isdigit():
			numbers.append(int(letter))
	return sum (numbers)


