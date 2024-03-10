#--------------
#</Gustavo Maciel>
#14/07/2023
#--------------
from aritmetica import flotar, loggar, intar
loggar('O Programa Pequenos Desafios foi Interpretado')

#DESAFIO BUSCA NA INTERNET
def num_pessoas_site():
	loggar('Função Busca na Internet Iniciou')
	print('Exercício 5.2 - Busca na Internet')
	def conti():
		loggar('Sub-rotina Conti solicitada')
		esc = 9;
		while esc not in ['s', 'n']:
			esc = str(input('\n(S/N)? > ')).strip().lower()
			loggar(f'Usuário: {esc}')
		return True if esc == 's' else False
	def program():
		t = -1
		while not (0 <= t <= 1000):
			print('"t" de ser maior que 0 e menor que mil')
			print('Digite o Valor de "t"',end=''); t = intar()
		print(f'O Número de pessoas que clicaram no Primeiro Site é {t*4}')
		print(f'''LISTA INDEX
1º Site: {t*4}
2º Site: {t*2}
3º Site: {t}
4º Site: {t/2}
		''')
		print('Desenja Continuar?',end='')
		loggar('Sub-rotina Conti a ser chamada...')
		return conti()
	while True:
		if not program():
			break
	loggar('Fim da Função Busca na Internet')

#DESAFIOS TOMADAS
def desafio_tomadas():
	loggar('Função Desafio Tomadas Iniciou')
	print('Exercício 5.3 - Desafio: Tomadas')
	qto, tot, li = -1, -1, []
	while qto < 1:
		print('Digite o número de extensões que possuí: ',end=''); qto = intar()
	for c in range(qto):
		while not (1 <= tot <= 6):
			print(f'Digite o Nº de Tomadas da {c+1}º extensão abaixo.')
			tot = intar()
		li.append(tot); tot = -1
	print('Calculando o número de tomadas disponíveis')
	print(f'Total de Tomadas Livres: {sum(li) - (qto - 1)}')
	loggar(f'Livres: {sum(li) - (qto -1)}')
	loggar('Fim da Função Desafio Tomadas')

#DESAFIO: PONTUAÇÃO BASQUETE
def pontu_basquete():
	loggar(f'Função Pontuação Basquete Iniciou')
	print(f'Exercício 5.4 - Pontuação Basquete')
	qto, li, listb, tot = -1, [], [], -1
	print('Quantos Jogos?')
	while tot <= 0:
	    tot = intar()
	for c in range(tot):
		print(f'{c+1}º Jogo',end=''); qto = intar()
		li.append(qto)
	listb = li[1:]
	print(f'Melhor Jogo "{max(listb)}" = {listb.index(max(listb))+2}º Jogo')
	print(f'Pior Jogo "{min(li)}"" = {li.index(min(li))+1}º Jogo')
	record = 0
	melhor = li[1]
	# Começa do segundo jogo, pois o primeiro jogo não conta como novo recorde do melhor
	for i in range(1, len(listb)):
		if li[i] > melhor:
			melhor = li[i]
			record += 1
	print(f'Número de vezes que quebrou o recorde: {record}')
	loggar(f'Melhor {max(listb)} | Pior {min(li)}| Records {record}')
	loggar('Fim da Função Pontuação Basquete')















