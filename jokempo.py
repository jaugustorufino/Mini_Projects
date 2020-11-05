from random import randint

def check(move):
	while True:
		if move != 'pedra' and move != 'papel' and move != 'tesoura':
			move = input('Erro!\nDigite um movimento válido! ')
		else:
			break

	return move


def jokempo():
	while True:
		move2 = input('Digite seu movimento (pedra/papel/tesoura)\n' + ' ' * 8)
		move2 = check(move2)
		mv1 = randint(1,3)
		move1 = d[mv1]

		if move2 == 'pedra' and move1 == 'tesoura':
			print(f'Parabéns, você ganhou! :)\nO movimento escolhido pelo programa foi: {move1}')

		elif move2 == 'papel' and move1 == 'pedra':
			print(f'Parabéns, você ganhou! :)\nO movimento escolhido pelo programa foi: {move1}')

		elif move2 == 'tesoura' and move1 == 'papel':
			print(f'Parabéns, você ganhou! :)\nO movimento escolhido pelo programa foi: {move1}')

		elif move1 == move2:
			print('Empate :|')

		else:
			print(f'Você perdeu! :(\nO movimento escolhido pelo programa foi: {move1}')

		p_ag = input('Play Again? (y/n) ')
		
		if p_ag.lower() != 'y':
			break

d = {
	1: 'pedra',
	2: 'papel',
	3: 'tesoura'
}

jokempo()