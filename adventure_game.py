d = {}
d[0] = [1,2]
d[1] = 'se fudeu','Voltar? (y/n) '
d[2] = [3,4]
d[3] = 'se fudeu','Voltar? (y/n) '
d[4] = [5,6]
d[5] = [7,8,9]
d[6] = 'se fudeu','Voltar? (y/n) '
d[7] = 'se fudeu','Voltar? (y/n) '
d[8] = 'Acertou, mizeravel!'
d[9] = 'se fudeu','Voltar? (y/n) '

i = 0
anterior = 0

while True:
	if 'se fudeu' in d[i]:
		print('\n' + 'se fudeu')
		a = input(d[i][1])
		if a == 'y':
			print(f'Considerando essas portas: {d[anterior]}')
			porta = int(input('Para qual delas deseja ir? '))
		
		else:
			break

	elif d[i] == 'Achooou!':
		print('\n' + d[i])
		break

	else:
		print(f'Considerando essas portas: {d[i]}')
		porta = int(input('Para qual delas deseja ir? '))
	
	anterior = i
	i = porta