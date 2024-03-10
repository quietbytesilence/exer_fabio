#--------------
#</Gustavo Maciel>
#19/06/2023
#--------------
#EXECICIOS ESTRUTURAS DE MATRIZES
from aritmetica import flotar, intar, loggar
loggar('O Programa Estruturas de Matrizes foi Interpretado!')
#ORDEM INVERSA
def inversa_ordem():
	loggar('Função Ordem Inversa Iniciou')
	print('Exercício 4.1 - Ordem Inversa')
	print('Digite valores abaixo, seprado por ","(Vírgula)')
	num = str(input('Digite: ')).split(',')
	print('Os valorena ordem inversão são:')
	for c in range(len(num),0,-1):
		print(f'{c}º - {num[c-1]}')
		loggar(f'{c} - {num[c-1]}')
	loggar('Fim da Função')

#PRODuTO DA MATRIZ -V1
def prod_matriz():
	loggar('Função Produto da Matriz Iniciou')
	print('Exercício 4.2 - Produto da Matriz')
	print('20 Valores abaixo:');lista = []
	for c in range(20):
		print(f'Digite {c+1}º valor'); a = flotar()
		lista.append(a)
	print('Digite a Constate Multiplicativa: ');a = intar()
	loggar(f'Matriz: {lista}')
	for c in range(20):
		j = lista[c]; lista.remove(j)
		j = j*a; lista.insert(c,j)
		print(f'{c+1}º = {lista[c]}')
	loggar(f"Matriz': {lista}")
	loggar('Fim da Função')

#PRODUTO DA MATRIZ - V2
def prod_matri_dois():
	loggar('Função Produto Matriz - V2 Iniciou')
	print('Exercício 4.3 - Produto da Matriz - V2');k = range(20)
	print('Digite a Constante Multiplicativa '); a = intar()
	print('Digite 20 Valores Abaixo:'); lista, listb = [], []
	for c in k:
		print(f'Digite o {c+1}º Termo: '); b = flotar()
		lista.append(b); listb.append(float(a*b))
		loggar(f'Lista A: {lista}')
		loggar(f'Lista B:{listb}')
	for c in k:
		print(f'{c+1}º  Termo: {lista[c]} * {a} = {listb[c]} ')
	loggar('Fim da Função')

#PESQUISA DE VALORES
def pesquisa_val():
	loggar('Função Pesquisa de Valores Iniciou')
	def conti():
		loggar('Sub-rotina Conti solicitada')
		esc = 9;
		while esc != 's' and esc != 'n':
			esc = str(input('(S/N)? > ')).strip().lower()
			loggar(f'Usuário: {esc}')
		return True if esc == 's' else False
	print('Exercício 4.4 - Pesquisando Valor')
	print('Quantos valores? ', end=''); k, lista = intar(), []
	for c in range(0,k):
		print(f'{c+1}º: ',end=''); a = flotar()
		lista.append(a)
	while True:
		print('Qual valor deseja checar? ',end=''); term = flotar()
		loggar(f'Usuário quer checar {term}')
		if term in lista:
			print(f'O termo encontra-se na {lista.index(term)+1}º Posição')
			loggar(f'Found! {lista.index(term)} in {lista}')
		else:
			print('Termo não encontrado')
			loggar('404')
		print('Desenja Continuar?',end='')
		loggar('Sub-rotina Conti a ser chamada...')
		if not conti():
			loggar('Fim da Função')
			break

#LISTAR SOMENTE MULHERES
def somen_mulher():
	loggar('Fução Listar Somente Mulheres Iniciou')
	print('Exercício 4.5 - Listando as Mulheres')
	nome, sexo, idade = [], [], []
	for c in range(20):
		loggar("Sub-rotina de Input's iniciada")
		s, i = 'j', -9; n = str(input('Nome: ')).strip().title()
		while s != 'f' and s != 'm':
			s = str(input('Sexo: (M/F) > ')).strip().lower()
			loggar(f'Usuário Input: {s}')
		while i < 0 or i > 100:
			print('Idade: ',end='');i = intar()
		nome.append(n)
		idade.append(i)
		sexo.append(s)
	for j, (n, s, i) in enumerate(zip(nome, sexo, idade)):
		frase = f'Nome: {n} | Idade: {i} | Sexo: {s}' if s == 'f' else ''
		loggar(f'{j+1} = {frase}')
		print(frase)
	loggar('Fim da Fução Listar Somente Mulheres')

#LISTAR SOMENTE MAIORES DE 18 ANOS
def somen_18():
	loggar('Função Listar Maiores de 18 Anos Iniciou')
	print('Exercício 4.5 - Listando Maiores de 18 anos')
	nome, sexo, idade = [], [], []
	for c in range(20):
		loggar("Sub-rotina de Input's iniciada")
		s, i = 'j', -9; n = str(input('Nome: ')).strip().title()
		while s != 'f' and s != 'm':
			s = str(input('Sexo: (M/F) > ')).strip().lower()
			loggar(f'Usuário Input: {s}')
		while i < 0 or i > 100:
			print('Idade: ',end='');i = intar()
		nome.append(n)
		idade.append(i)
		sexo.append(s)
	for j, (n, s, i) in enumerate(zip(nome, sexo, idade)):
		frase = f'Nome: {n} | Idade: {i} | Sexo: {s}' if i > 18 else ''
		loggar(f'{j+1} = {frase}')
		print(frase)
	loggar('Fim da Fução Listar Somente Maiores de 18 Anos')

#LISTAR MAIORES DE 18 - V2
def somen_18_dois():
	loggar('Função Listar Maiores de 18 Anos Iniciou')
	print('Exercício 4.6 - Listando Maiores de 18 Anos - V2')
	qto, s, i, li, k = -1, 'j', -9, [], 0
	while qto <= 0:
		print('Quantas Pessoas deseja Adicionar? ',end=''); qto = intar()
	for _ in range(qto):
		loggar("Sub-rotina de Input's iniciada")
		pessoa = {}
		n = str(input('NOME: ')).strip().title()
		while s not in ['f', 'm']:
			s = str(input('SEXO (F/M): ')).strip().lower()
			loggar(f'Usuário Input: {s}')
		while i <= 0 or i > 100:
			print('IDADE: ',end=''); i = intar()
		pessoa['idade'] = i
		pessoa['sexo'] = s
		pessoa['nome'] = n
		s, i, n = 'j', -9, ''
		li.append(pessoa)
	loggar('sorting Itens of List')
	li.sort(key=lambda pessoa: pessoa['idade'], reverse=True)
	loggar('Done!'); loggar(f'{li}')
	for pessoa in li:
		frase = f"Nome: {pessoa['nome']}\n Sexo: {pessoa['sexo']}\n Idade: {pessoa['idade']}"
		frase = frase if pessoa['idade'] > 18 else ''
		print('#',20*'=','\n',frase)
		k = k + 1 if len(frase) > 1 else k
		loggar(f'{k} - {frase}')
	print(f'\n\nTotal de pessoas: {qto}'); loggar(f'Total: {qto}')
	print(f'Total de pessoas listadas: {k}'); loggar(f'P.L: {k}')
	print(f'Um total de {(k/qto)*100:.1f}% das pessoas foram listadas')
	loggar('Fim da Fução Listar Somente Maiores de 18 Anos')

#ORDEM CRESCENTE
def crece_ordem():
	loggar(f'Função Ordem Crescrente Iniciou')
	print('Exercício 4.7 - Ordem Crescrente'); lista = []
	print('Quantos valores deseja comparar? ',end=''); qto = intar()
	loggar("Sub-rotina de Input's iniciada")
	for c in range(0, qto):
		print(f'{c+1}º: ',end=''); a = flotar()
		lista.append(a)
	loggar('sorting Itens of List')
	lista.sort(); loggar('Done!');
	loggar(f'{lista}')
	print('Valores organizados abaixo: \n')
	for i, item in enumerate(lista):
		print(f'{i+1}º = {item}')
	loggar('Fim da Função Ordem Crescrente')

#ORDEM DECRESCENTE
def decresce_ordem():
	loggar('Função Ordem Decrescrente Iniciou')
	print('Exercício 4.8 - Ordem Decrescrente'); lista = []
	print('Quantos valores deseja comparar? ',end=''); qto = intar()
	loggar("Sub-rotina de Input's iniciada")
	for c in range(0, qto):
		print(f'{c+1}º: ',end=''); a = flotar()
		lista.append(a)
	loggar('sorting Itens of List')
	lista.sort(reverse=True)
	loggar('Done!'); loggar(f'{lista}')
	print('Valores organizados abaixo: \n')
	for i, item in enumerate(lista):
		print(f'{i+1}º = {item}')
	loggar('Fim da Função Ordem Decrescrente')

#ORDEM ALFABÉTICA
def alfabe_ordem():
	loggar('Função Ordem Alfabética Iniciou')
	print('Exercício 4.9 - Ordem Alfabética'); lista = []
	print('Quantos valores deseja comparar? ',end=''); qto = intar()
	loggar("Sub-rotina de Input's iniciada")
	for c in range(0, qto):
		print(f'Insira o {c+1}º valor: ',end=''); a = str(input('>>>> ')).strip().title()
		if len(a) != 0:
			lista.append(a)
	loggar('sorting Itens of List')
	lista.sort(key=str.lower)
	loggar('Done!'); loggar(f'{lista}')
	print('Valores organizados abaixo: \n')
	for i, item in enumerate(lista):
		print(f'{i+1}º = {item}')
	loggar('Fim da Função Ordem Alfabética')

#MAIS NOVOS PRIMEIRO
def mais_novos():
	loggar('Função Mais Novos Primeiro Iniciou')
	print('Exercício 4.10 - Mais Novos Primeiro')
	qto, s, i, li, k = -1, 'j', -9, [], 0
	while qto <= 0:
		print('Quantas Pessoas deseja Adicionar? ',end=''); qto = intar()
	loggar("Sub-rotina de Input's iniciada")
	for _ in range(qto):
		pessoa = {}
		n = str(input('NOME: ')).strip().title()
		while s not in ['f', 'm']:
			s = str(input('SEXO (F/M): '))
		while i <= 0 or i > 100:
			print('IDADE: ',end=''); i = intar()
		pessoa['idade'] = i
		pessoa['sexo'] = s
		pessoa['nome'] = n
		s, i, n = 'j', -9, ''
		li.append(pessoa)
	loggar('sorting Itens of List')
	li.sort(key=lambda pessoa: pessoa['idade'], reverse=False)
	loggar('Done!'); loggar(f'{li}')
	for pessoa in li:
		pessoa['sexo'] = 'Masculino' if pessoa['sexo'] == 'm' else 'Feminino'
		frase = f"Nome: {pessoa['nome']}\n Sexo: {pessoa['sexo']}\n Idade: {pessoa['idade']}"
		#frase = frase if pessoa['idade'] > 18 else ''
		print('#',20*'=','\n',frase)
		k = k + 1 if len(frase) > 1 else k
		loggar(f'{k} - {frase}')
	print(f'\n\nO total de pssoas: {qto}')
	loggar(f'Listadas: {k}')


#IDEA: Criar função com argumento para automatizar o logging.info('Mensagem')
"""def loggar(msg):
	logging.info(msg)"""
#============================FEITO!