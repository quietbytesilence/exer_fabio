#--------------
#</Gustavo Maciel>
#18/06/2023
#--------------
#EXERCÍCIOS DE ESTRUTRAS DE REPETIÇÃO
from aritmetica import flotar, intar, loggar
from math import factorial
loggar('O Programa Estruturas de Repetição foi Interpretado!')
#APENAS POSITIVO
def apena_posi():
	loggar('Função Apenas Positivos Iniciou')
	print('Exercício 3.1 - Apenas Positivos'); valores = []
	print('Quantos Número deseja digitar?',end=''); qto = flotar()
	for c in range(1,qto+1):
		while True:	
			print(f'Digte o {c}º Número ',end='');a = flotar()
			if a < 0:
				print('Valopr Inválido!. Por Favor insira um Positivo')
				loggar(f'Erro do User -> {a}')
			else:
				break
		valores.append(a); a = None
	print(f'Os valores Digitados foram{valores}')
	print(f'A soma do todos é {sum(valores)}')
	loggar(f'Inputs Válido: {valores}\nSoma Total: {sum(valores)}')

#SEGUNDO MAIOR QUE PRIMEIRO
def segundo_maior():
	loggar('Função Segundo Maior Iniciou')
	print('Exercício 3.2 - Segundo Maior que o Primeiro')
	print('Digite um número ',end=''); a = flotar()
	print('Digite outro número'); b = flotar()
	while a >= b:
		print('O Segundo Número deve ser maior que o primeiro.')
		print('Digite Novamente ',end='');b = flotar()
	print(f'Número 1 = {a}\nNúmero 2 = {b}')
	loggar(f' {a} > {b}')

#SEXO F OU M
def sexo_f_m():
	print('Exercício 3.3 - Sexo F ou M');sexo = ''
	print('DIGITE SEU SEXO:\n[F] - Feminino\n[M] - Masculino')
	while sexo != 'f' and sexo != 'm':
		sexo = str(input('>> ')).strip().lower()
		loggar(f'User setou {sexo}')
	texto = 'lo' if sexo == 'm' else 'la'
	print(f'Prazer em conhecê-{texto}!')

#TABUADA DO 5
def tabu_cinco():
	print('Exercício 3.4 - Tabuada do 5')
	print('#'+9*'='+'#'); loggar('Função Tabuda do 5 Iniciou')
	for c in range (1,6):
		print(f'5 x {c} = {c*5}')
	print('#'+9*'='+'#\n'); loggar('Fim da Função Tabuda do 5')

#TABUADA DE N | NÚMERO POISITIVO (1-10)
def tabu_dez():
	loggar('Tabuda de 10 de N Iniciou')
	print('Exercício 3.5 - Tabuda de Positivo (1-10)')
	while True:
		print('Digite um número inteiro maior que 0')
		num = flotar()
		if num > 0:
			break
		loggar('Usuário errou o preenchimento')
	print('#'+9*'='+'#'); loggar('Calculando...')
	for c in range(1,11):
		print(f'{num} x {c} = {num*c}')
	print('#'+9*'='+'#\n'); loggar('Fim da Função Tabuda de 10 de N')

#TABUADA PARCIAL DE UM NÚMERO
def tabuada_parcial():
	loggar('Função Tabuda Parcial de um Número Iniciou')
	print('Exercício 3.6 - Tabuada Parcial de um Número')
	print('Todos os Números devem ser Positivos\nO Último termo deve ser maior que segundo')
	a, b, c = -1, -1, -1
#	while a <= 0 or b <= 0 or c <= 0 or c < a: #while min(a, b, c) <= 0 or c < a:?
	while a <= 0:
		print('Digite o número gerador ',end=''); a = flotar()
	while b <= 0:
		print('Digite o primeiro primeiro multiplicador da tabuada ',end=''); b = flotar()
	while c < b:
		print('Digite o o úlimo multiplicador da tabuda ',end=''); c = flotar()
	print('#'+9*'='+'#'); loggar(f'a = {a}, b = {b}, c = {c}')
	for c in range(int(b),int(c + 1)):
		print(f'{a} x {c} = {a*c}')
	print('#'+9*'='+'#\n'); loggar('Fim da Função Tabuda Parcial de um Número')

# SOMA DE 1 A 100
def sumacem():
	loggar('Função Soma de 1 a 100 Iniciou')
	print('Exercício 3.7 - Soma de 1 a 100'); soma =  1
	for g in range(2, 101):
		soma = soma + g
	print(f'A soma de todos de dígitos de 1 a 100 é: {soma}')
	loggar(f'Soma = {soma}'); loggar('Fim da Função Soma de 1 a 100')

#Fibonacci
def fibonacci():
	print('Exercício 3.8 - Fibonacci'); loggar('Função Fibonacci Iniciou')
	print('Quantos número da sequência Fibonacci deseja? ',end='');qto = flotar()
	lista = [1, 1]
	for c in range(1, int(qto-1)):
		a = lista[-2] + lista[-1]
		lista.append(a)
	loggar(f'User setou {qto}'); loggar(lista)
	for g, num in enumerate(lista):
		tam = len(str(g))
		ta = ' ' if g < 9 else ''
		print(f'{ta}{g + 1}º = {num}')
	loggar('Fim da Função Fibonacci')

# SERIE DE BERGAMASCHI
def bergamaschi():
	loggar('Função Bergamaschi Iniciou')
	print('Exercício 3.9 - Bergamaschi')
	print('Quantos número da sequência Bergamaschi deseja? ',end='');qto = flotar()
	lista = [1, 1, 1]; loggar(f'User setou {qto}'); loggar('Calculando...')
	for c in range(1, int(qto+1)):
		a = lista [-3] + lista[-2] + lista[-1]
		lista.append(a)
	for g, num in enumerate(lista):
		tam = len(str(g))
		ta = ' ' if g < 9 else ''
		print(f'{ta}{g + 1}º = {num}')
	loggar(lista); loggar('Fim da Função Bergamaschi')

# N NÚMEROS DA SEQUÊNCIA - V1
def num_seq():
	loggar('Função Números da Sequência - V1 Iniciou')
	print('Exercício 3.10 - N Números da Sequência - V1')
	print('Digite um número inteiro < 100 ',end=''); n = 400
	while n > 100:
		print('Digite Um Número Inteiro Menor que 100')
		n = int(intar())
	seq, d = [], 0;
	print(f'Número a Considerar: {n}')
	for c in range(1, n+1):
		seq.append(int(c**2 + 1))
		d = d + seq[-1]
	print(f'A soma dos valores setados nesse intervalo é: {d}')
	print(25*'=', '\n'); loggar(f'Soma dos Valores: {d}')
	for i in range(0, len(seq)):
		ta = ' ' if i < 9 else ''
		print(f'{ta}{i + 1}º = {seq[i]}')
	loggar('Fim da Função Números da Sequência - V1')

#N NÚMEROS DA SEQUÊNCIA - V2
def num_seq_dois():
	loggar('Função Números da Sequência - V2 Iniciou')
	print('Exercício 3.11 - N Números da Sequência - V2')
	b, a , k = [], [], 80
	while k > 50 and k <= 0:
		print('Digite um Número Inteiro Menor que 50')
		k = intar()
	for c in range(1, k + 1):
		ta = ' ' if c < 10 else ''
		a.append(str(f'{c}{ta} / {c+1}'))
		j = float(c/(c+1))
		b.append(j)
	for i in range(0, len(b)):
		ta = ' ' if i < 9 else ''
		print(f'{ta}{i+1}º = {a[i]}')
	print(f'a soma total é: {sum(b)}')
	loggar(f'Soma: {sum(b)}')
	loggar('Fim da Função Números da Sequência - V2')

# N NÚMEROS DA SEQUÊNCIA - V3
def num_seq_tres():
	loggar('Função N Números da Sequência - V3 Iniciou')
	print('Exercício 3.12 - N Números da Sequência - V3')
	b, a , k = [], [], 80
	while k > 50:
		print('Digite um Número Inteiro Menor que 50')
		k = intar()
	for c in range(1, k + 1):
		if int(len(str(c**2+1))) == 1:
			ta = '  '
		elif int(len(str(c**2+1))) == 2:
			ta = ' '
		else:
			ta = ''
		a.append(str(f'{c**2 + 1}{ta} / {c**3}'))
		j = float((c**2 + 1)/(c**3))
		b.append(j); loggar('Calculando...')
	for i in range(0, len(b)):
		ta = ' ' if i < 9 else ''
		print(f'{ta}{i+1}º = {a[i]}')
	print(f'a soma total é: {sum(b)}')
	loggar(f'Soma: {sim(b)}')
	loggar('Fim da Função N Números da Sequência - V3')

#MAIOR, SOMA E MÉDIA DE 3 VALORES
def maior_soma_media():
	print('Exercício 3.13 - Maior, Soma e Média')
	print('Digite números abaixo: ');a, b = [], 0;
	for c in range(0, 3):
		print(f'{c+1}º = ',end='');b = flotar();
		while b >= 20 or b < 0:
			print('Digite um número menor que 20')
			print(f'{c+1}º = ',end='');b = flotar();
		a.append(b)
	print(f'O maior valor Digitado Válido foi: {max(a)}')
	print(f'O menor valor Digitado Válido foi: {min(a)}')
	print(f'A média aritmética desses valores é: {(a[0]+a[1]+a[2])/3:.2f}')


def maior_soma_media_ad_infinitum():
	loggar('Função Maior, Soma, Média e Porcentagem Recursiva Iniciou')
	print('Exercício 3.14 - Maior, Soma, Média e Porcentagem -v1')
	print('Quantos números deseja? ',end='');j = intar()
	print('Digite números abaixo: ');a, b = [], 0;
	for c in range(0, (j)):
		print(f'{c+1}º = ',end='');b = flotar();
		while b >= 20 :
			print('Digite um número menor que 20')
			print(f'{c+1}º = ',end='');b = flotar();
		a.append(b)
	loggar(a); loggar(f'Max: {max(a)} | Min: {min(a)}')
	print(f'O maior valor Digitado Válido foi: {max(a)}')
	print(f'O menor valor Digitado Válido foi: {min(a)}');nega, posi = [], []
	print(f'A média aritmética desses valores é: {(sum(a))/(len(a)):.2f}')
	for c in range(0, len(a)):
		if a[c] < 0:
			nega.append(a[c])
		elif a[c] >= 0:
			posi.append(a[c])
	n = len(nega);p = len(posi)
	pp, pn = 0, 0;
	if n != 0:
		pp = (p/len(a)) * 100
	if p != 0:
		pn = (n/len(a)) * 100
	loggar(f'Média: {sum(a)/len(a)}'); loggar(pp, pn)
	print(f'Existem {pp:.1f}% números positivos')
	print(f'Existem {pn:.1f}% números negativos')
	loggar('Fim da Função Maior, Soma, Média e Porcentagem Recursiva Iniciou')

#MAIOR, MENOR, MÉDIA E PORCENTAGEM
def maior_soma_media_ad_infinitum_recursiva():
	loggar('Função Maior, Média, Soma e Porcentagem - V2 Iniciou')
	def program():
		print('Exercício 3.15 - Maior, Soma, Média e Porcentagem -v2')
		print('Quantos números deseja? ',end='');j = intar()
		print('Digite números abaixo: ');a, b = [], 0;
		loggar("Sub-rotina de Input's iniciada")
		for c in range(0, (j)):
			print(f'{c+1}º = ',end='');b = flotar();
			while b >= 20 :
				print('Digite um número menor que 20')
				print(f'{c+1}º = ',end='');b = flotar();
			a.append(b)
		loggar(a)
		print(f'O maior valor Digitado Válido foi: {max(a)}')
		print(f'O menor valor Digitado Válido foi: {min(a)}');nega, posi = [], []
		print(f'A média aritmética desses valores é: {(sum(a))/(len(a)):.2f}')
		for c in range(0, len(a)):
			if a[c] < 0:
				nega.append(a[c])
			elif a[c] >= 0:
				posi.append(a[c])
		p = len(nega);n = len(posi)
		pp, pn = 0, 0;
		if n != 0:
			pp = (p/len(a)) * 100
		if p != 0:
			pn = (n/len(a)) * 100
		loggar('Done!')
		print(f'Existem {pp:.1f}% números positivos')
		print(f'Existem {pn:.1f}% números negativos');
		logar('Fim Deamon'); escolha()
	def escolha():
		loggar('Deamon Continução')
		esc = 'j'
		print('\nDeseja uma nova instância do programa? (s/n)')
		while esc != 's' and esc != 'n':
			print('Responda com "S" ou "N"')
			esc = str(input('>>> ')).strip().lower()
		if esc == 's':
			loggar(f'User: {esc}')
			program()
		else:
			print('\n')
			loggar('Fim da Função Maior, Média, Soma e Porcentagem - V2 Iniciou')
	program()

#CALCULAR FATORIAL
def fatorial():
	loggar('Função Fatorial Iniciou')
	def program():
		print('Exercício 3.16 - Fatorial'); n = 0
		print('Digite um número para ver seu fatorial')
		while n <= 0:
			print('>>> ',end=''); n = intar()
		print(f'{n}! = {factorial(n)}')
		loggar(f'User: {n}'); escolha()
	def escolha():
		esc = 'j'; loggar('Deamon Continução')
		print('\nDeseja uma nova instância do programa? (s/n)')
		while esc != 's' and esc != 'n':
			print('Responda com "S" ou "N"')
			esc = str(input('>>> ')).strip().lower()
		if esc == 's':
			program()
		else:
			print('\n'); loggar('Fim da Função Fatorial')
	program()
