import sys

def collatz(number):
	if number % 2 == 0:
		x = number / 2
	elif number % 2 == 1:
		x = 3 * number + 1
	else:
		print('You did not enter an integer.')
		sys.exit()
	return x

print('Please enter a positive integer: ')
y = input()
y = int(y)

while y != 1:
	y = collatz(y)
	print(y)
