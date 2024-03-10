#--------------
#</Gustavo Maciel>
#18/06/2023
#--------------
#Esse aquivo é uma dependência geral
#--------------
#EXERCÍCIOS DE ARITMÉTICA
import math, logging
logging.basicConfig(filename='logging_program.log', 
					level=logging.INFO, 
					format='%(asctime)s - %(levelname)s - %(message)s', 
					datefmt='%d-%b-%y %H:%M:%S')
logging.info('O Programa Aritmética foi Interpretado!')
def loggar(msg):
	logging.info(msg)
def flotar():
	loggar('Função Flotar Solicitada')
	num = None
	while True:
		valor = input('>>>> ').strip()
		loggar(f'O Usuário inseriu: "{valor}" para flotar()')
		try:
			num = float(valor)
			break
		except ValueError:
			print('Valor Inválido! Por favor insira um número.')
			loggar('Erro de Input')
	return num;
def intar():
	loggar('Função Intar Solicitada')
	num = None
	while True:
		valor = input('>>>> ').strip()
		loggar(f'O Usuário inseriu: "{valor}" para intar()')
		if valor.isdigit():
			num = int(valor)
			break
		else:
			print('Valor Inválido! Por favor insira um número inteiro.')
			loggar('Erro de Input')
	return num;
#ÁREA DO RETÂNGULO
def area_retangulo():
	loggar('Área do Retângulo Iniciou')
	print('Exercício 1.1 - Área do Retângulo')
	print('Digite abaixo a base e altura do retângulo.')
	print('Digite a altura ',end=''); alt = flotar()
	print('Digite a Base ',end=''); base = flotar()
	print(f'\nA Área do Retângulo é de {alt*base:.2f} U² (Unidades Quadradas)\n')
	loggar(f'Fim do função return: {alt*base:.2f}')

#ÁREA DO QUADRADO V-1
def area_quadrado():
	loggar('Área do Quadrado Iniciou')
	print('Exercício 1.2 - Área do Quadrado')
	print('Digite abaixo a aresta do Quadrado')
	aresta = flotar()
	print(f'\nA Área do Quadrado é de {aresta*aresta:.2f} U² (Unidades Quadradas)\n')
	loggar(f'Fim do função return: {aresta*aresta:.2f}')

#ÁREA DO QUADRADO V-2
def area_quadrado_dois():
	loggar('Função Área do Quadrado Dois')
	print('Exercício 1.3 - Área do Quadrado (cálculo pela Diagonal)')
	print('Digite abaixo o valor da Diagonal do Quadrado\n')
	dig = flotar()
	print(f'A Área do Quadrado é de {(dig*dig)/2:.2f} U²(Unidades Quadradas)\n')
	loggar(f'Fim do função return: {(dig*dig)/2:.2f}')

#ÁREA DO TRIÂNGULO
def area_triangulo():
	loggar('Função Área do Triângulo Iniciou')
	print('Exercício 1.4 - Área do Triângulo')
	print('Digite a Altura do Triângulo ',end=''); alt = flotar()
	print('Digite a Base do Triângulo ',end=''); base = flotar()
	print(f'A Área do Triangulo é de {(alt*base)/2:.2f} U² (Unidades Quadradas)\n')
	loggar(f'Fim do função return: {(alt*base)/2:.2f}')

#VOLUME DA ESFERA
def volume_esfera():
	loggar('Função Volume da Esfera Iniciou')
	print('Exercício 1.5 - Volume da Esfera')
	print('Digite o Diâmetro da Esfera ',end=''); dia = flotar()
	print(f'O Volume da Esfera é de {(4/3) * math.pi * ((dia/2)**3)} U³ (Unidades Cúbicas)\n')
	loggar(f'Fim do função return: {(4/3) * math.pi * ((dia/2)**3)}')

#MÉDIA ARITMÉTICA
def media_aritmetica():
	loggar('Função Média Aritmética Iniciou')
	print('Exercício 1.6 - Média Aritmética')
	print('Digite 4 (Quatro) valores abaixo:')
	print('1º Valor ',end=''); v1 = flotar()
	print('2º Valor ',end=''); v2 = flotar()
	print('3º Valor ',end=''); v3 = flotar()
	print('4º Valor ',end=''); v4 = flotar()
	print(f'A Média Aritmética desses valores é de {(v1+v2+v3+v4)/4:.2f}\n')
	loggar(f'Fim do função return: {(v1+v2+v3+v4)/4:.2f}')

#MÉDIA GEOMÉTRICA DE DOIS VALORES
def media_geometrica():
	loggar('Função Média Geométrica Iniciou')
	print('Exercício 1.7 - Média Geométrica')
	print('Digite abaixo dois valores para a média')
	print('1º Valor ',end=''); v1 = flotar()
	print('2º Valor ',end=''); v2 = flotar()
	print(f'A Média Geométrica desses valores é {(v1*v2)**(1/2):.2f}\n')
	loggar(f'Fim do função return: {(v1*v2)**(1/2):.2f}')

#MILHAS VS KILÔMETROS
def milhas_quilometros():
	loggar('Milhas vs Kilômetros Iniciou')
	print('Exercício 1.8 - Milhas vs Km')
	print('''
		Escolha a opção desejada:
		[1] - Km -> Milhas
		[2] - Milhas -> Km
		''')
	while True:
		esc = flotar()
		if esc == 1:
			print('Digite o valor em Km ',end=''); valor = flotar(); p = '' if valor == 1 else 's'
			print(f'\n{valor:.2f} Kilômetro{p} = {valor * 0.621371:.2f} Milha{p}\n')
			loggar(f'Fim do função return: {valor * 0.621371:.2f}');break
		elif esc == 2:
			print('Digite o valor em Milhas ',end=''); valor = flotar(); p = '' if valor == 1 else 's'
			print(f'\n{valor:.2f} Milha{p} = {valor * 1.60934:.2f} Kilômetro{p}')
			loggar(f'Fim do função return: {valor * 1.60934:.2f}');break
		else:
			print('Inválido!\nO valor tem que ser 1 ou 2')

#LEI DE OHM
def lei_ohm():
	loggar('Função Lei de Ohm Iniciou')
	print('Exercício 1.9 - Lei de Ohm')
	print("Digite o valor da resistência em Ω Ohm's ",end=''); r = flotar()
	print('Digite o valor da corrente em A amperes ',end=''); c = flotar()
	print(f'O valor da Tensão (V) é {r*c:.2f}\n')
	loggar(f'Fim do função return: {r*c:.2f}')

#Celsius vs Fahrenheit
def celsius_fahrenheit():
	loggar('Função Celsius vs Fahrenheit Iniciou')
	print('Exercício 1.10 - Celsius vs Fahrenheit')
	print('''
		Escolha a opção desejada:
		[1] - Celsius °C -> Fahrenheit °F
		[2] - Fahrenheit °F -> Celsius °C
		''')
	while True:
		esc = flotar()
		if esc == 1:
			print('Digite o valor em °C ',end=''); valor = flotar()
			print(f'{valor:.1f} °C = {((valor * (9/5))+32):.1f} °F\n')
			loggar(f'Fim do função return: {((valor * (9/5))+32):.1f}');break
		elif esc == 2:
			print('Digite o valor em °F ',end=''); valor = flotar()
			print(f'{valor:.1f} °F = {((valor - 32) * 5/9):.1f} °C\n')
			loggar(f'Fim do função return: {((valor - 32) * 5/9):.1f}');break
		else:
			print('Inválido!\nO valor tem que ser 1 ou 2')

#ÁREA DO CÍRCULO
def area_circulo():
	loggar('Função Área do Círculo Iniciou')
	print('Exercício 1.11 - Área do Círculo')
	print('Digite o valor do Diâmetro ',end='');valor = flotar()
	print(f'Área do Círculo = {math.pi * ((valor/2)**2):.2f}\n')
	loggar(f'Fim do função return: {math.pi * ((valor/2)**2):.2f}')

#VOLUME DO CONE
def volume_cone():
	loggar('Função Área do Cone Iniciou')
	print('Exercício 1.12 - Volume do Cone')
	print('Digite o raio do Cone ',end=''); raio = flotar()
	print('Digite a altura do Cone ',end=''); alt  = flotar()
	print(f'O Volume do Cone é {math.pi * (1/3) * alt * raio ** 2:.2f} U³ (Unidades Cúbicas)\n')
	loggar(f'Fim do função return: {math.pi * (1/3) * alt * raio ** 2:.2f}')

#VELOCIDADE DO AUTOMÓVEL
def velocidade_automovel():
	loggar('Função Velocidade do Automóvel Iniciou')
	print('Exercício 1.13 - Velocidade do Automóvel')
	print('Digite os Dado abaixo:')
	print('Valor da Aceleração (m/s²) ',end=''); ace = flotar()
	print('Tempo de Percurso Segundos(s) ',end=''); se = flotar()
	print('Velocidade Inicial (m/s) ',end=''); ve = flotar(); k = (ve + (ace * se))*3.6
	print(f'A Velocidade Final do Automóvel é {k:.2f} k/h\n'); return k
	loggar(f'Fim do função return: {k:.2f}')

#VOLUME DO CUBO - VOLUME DA ESFERA CIRCUNSCRITA NO CUBO
def esfera_cubo():
	loggar('Função Esfera Cubo Iniciou')
	print('Exercício 1.14 - Volume do Cubo e da Esfera')
	print('Digite o Raio da Esfera ',end=''); r = flotar()
	print('Digite a Aresta(lado) do Cubo ', end=''); la = flotar()
	print(f'O volume Livre dentro do Cubo é de {(la ** 3) - (math.pi * (4/3) * (r**2))} U³ (Unidades Cúbicas)\n')
	loggar(f'Fim do função return: {(la ** 3) - (math.pi * (4/3) * (r**2))}')

#COTAÇÃO DO DÓLAR
def cotacao_dolar():
	loggar('Função Contação Dólar-Real Iniciou')
	print('Exercício 1.15 - Contação do Dólar')
	print('''
		[1] - Real -> Dólar
		[2] - Dólar -> Real
		''')
	while True:
		esc = flotar()
		if esc == 1:
			print('Digite o Valor da Cotação do Dólar ',end=''); do = flotar()
			print('Quantos Reais? ',end=''); re = flotar()
			print(f'R$: {re:.2f} = USD: {re/do:.2f}')
			loggar(f'Fim do função return: {re/do:.2f}');break
		if esc == 2:
			print('Digite o Valor da Cotação do Dólar ',end=''); do = flotar()
			print('Quantos Dólares? ',end=''); re = flotar()
			print(f'USD: {re:.2f} = R$: {re*do:.2f}')
			loggar(f'Fim do função return: {re*do:.2f}');break
		else:
			print('opção inválida!\nValores podem ser 1 ou 2')
		print('\n')

#FUNÇÕES TRIGNOMÉTRICAS
def trigonometricas():
	loggar('Funções Trigonométricas Iniciou')
	print('Exercício 1.16 - Funções Trigonométricas')
	print('Digite o Ângulo ',end=''); ag = math.radians(flotar())
	print(f'''
		Funções Trigonométricas de {ag:.4f}:
		Seno: {math.sin(ag):.4f}
		Cosseno: {math.cos(ag):.4f}
		Tangente: {math.tan(ag):.4f}
		Secante: {1/math.cos(ag):.4f}
		''')
	
#Exponencial e Logaritmo Natural
def expon_loga_nat():
	loggar('Função Função Exponencial e Logaritmo Natural Iniciou')
	print('Exercício 1.17 - Exponencial e Logaritmo Natural')
	print('Digite o valores abaixo:')
	print('X ',end=''); x = flotar()
	print('Y ',end=''); y = flotar()
	print(f'''
		x^y = {math.pow(x,y):.2f}
		Função Exp de X = {math.exp(x):.2f}
		Função Ln de X = {math.log(x):.2f}
		Função Exp de Y = {math.exp(y):.2f}
		Função Ln de Y = {math.log(y):.2f}
		''')

#COMPRA E TROCO
def compra_troco():
	loggar('Função Compra e Troco Iniciou')
	print('Exercício 1.18 - Compra e Troco'); lista = []
	print('Quantos Produtos? ',end=''); qto = int(flotar())
	for c in range(1, qto + 1):
		print(f'Digite o valor do {c}º Produto ',end=''); p = flotar()
		lista.append(p); p = 0;
	total = sum(lista)
	print(f'O valor total é R$ {total:.2f}')
	print('Valor do Pagamento ',end=''); pg = flotar()
	if pg < total:
		print(F'Falta pagar {total - pg:.2f}')
		loggar(f'Fim do função return: {total - pg:.2f}')
	elif pg >= total:
		print(f'Valor do troco R$: {pg - total:.2f}\nOBRIGADO PELA PREFERÊNCIA!')
		loggar(f'Fim do função return: {pg - total:.2f}')

#NOTA PARA APROVAÇÃO
def nota_aprova():
	loggar('Função Nota para Aprovação Iniciou')
	print('Exercício 1.19 - Nota para Aprovação')
	print('Digite a nota da 1º AV ',end=''); av1 = flotar()
	print(f'A nota necessária para aprovação é {(3 * 5.00 - av1)/2:.3f} pts\n')
	loggar(f'Fim do função return: {(3 * 5.00 - av1)/2:.3f}')
