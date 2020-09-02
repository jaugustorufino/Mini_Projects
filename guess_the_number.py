from random import randint

a = int(input('First Integer Parameter: '))
b = int(input('Second Integer Parameter: '))
n = randint(a, b)

while True:
	test = int(input('Guess! '))
	
	if test == n:
		print("You are right! Congratulations!")
		break
	
	if test < n:
		print('Too low...')
	
	else:
		print('Too High...')