	from aritmetica import logar
	a, b, c = [0,0,0], [0,0,0], [0,0,0];
	print(f'JOGO DA VELHA\n===============')
	def tabu():
		print('   0 1 2')
		print(f'A |{a[0]}|',end='');print(f'{a[1]}|',end='');print(f'{a[2]}|')
		print(f'B |{b[0]}|',end='');print(f'{b[1]}|',end='');print(f'{b[2]}|')
		print(f'C |{c[0]}|',end='');print(f'{c[1]}|',end='');print(f'{c[2]}|')
	tabu()

	#========================== VARIÁVEIS GLOBAIS E ESCOPO DE FECHAMENTO
	opcoes = ['a0', 'b0', 'c0', 'a1', 'b1', 'c1', 'a2', 'b2', 'c2']
	win = 0; t = 1
	n1 = str(input('Digite o Nome do Jogador 1: '))
	n2 = str(input('Digite o Nome do Jogador 2: '))
	loggar(f'P1: {n1} | P2: {n2}')
	#==========================
	#FUNÇÃO DE CHECAGEM ITERÁVEL
	#LÓGICA POICIONAL DE LISTA/MATRIZ N
	def checar(a, b, c):
		global win
		for i in range(0, 3):
			if (a[i] == b[i] == c[i]  in ['x', 'y']):
				if a[i] == 'x':
					print(f'Jogador {n1} Ganhou!');win = 1; loggar(f'{n1} Ganhou!');return win
				elif a[i] == 'y':
					print(f'Jogador {n2} Ganhou!');win = 1; loggar(f'{n2} Ganhou!');return win
		if (a[0] == a[1] == a[2] in ['x', 'y']) or (b[0] == b[1] == b[2] in ['x', 'y']) or (c[0] == c[1] == c[2] in ['x', 'y']):
			if a[0] == 'x' or b[0] == 'x' or c[0] == 'x':
				print(f'Jogador {n1} Ganhou!'); win = 1; loggar(f'{n1} Ganhou!');return win
			elif a[0] == 'y' or b[0] == 'y' or c[0] == 'y':
				print(f'Jogador {n2} Ganhou!'); win = 1; loggar(f'{n2} Ganhou!');return win
		elif (a[0] == b[1] == c[2] in ['x', 'y']) or (a[2] == b[1] == c[0] in ['x', 'y']):
			if b[1] == 'x':
				print(f'Jogador {n1} Ganhou!');win = 1; loggar(f'{n1} Ganhou!');return win
			elif b[1] == 'y':
				print(f'Jogador{n2} Ganhou!');win = 1; loggar(f'{n2} Ganhou!');return win
		elif 0 not in a and 0 not in b and 0 not in c:
			print('Empate')
			win = 1

	#VALIDADR DE VALORE PARA KEYWORDS --> Function checar
	def jogar():
		global n1, n2, opcoes, t, win
		print('Para Jogar você deve digitar posição que deseja preencher.\nEx. A1, C3...')
		p = 'j'
		def validar():
			global t
			nome = n1 if t == 1 else n2
			tipo = 'x' if t == 1 else 'y'
			print(f'É a vez de {nome} jogar'); posicao = None
			posicao = list(str(input('Digite a posição ')).strip().lower())
			if ''.join(posicao) in opcoes:
				print(posicao)
				opcoes.remove(''.join(posicao))
				if posicao[0] == 'a':
					a[int(posicao[1])] = tipo
				elif posicao[0] == 'b':
					b[int(posicao[1])] = tipo
				elif posicao[0] == 'c':
					c[int(posicao[1])] = tipo
				return 2 if t == 1 else 1
			else:
				print('Posição inválida. Tente novamente.')
				return t
		while True:
			t = validar()
			win = checar(a, b, c)
			tabu()
			if win == 1:
				break
	jogar()
