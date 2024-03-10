#--------------
#</Gustavo Maciel>
#19/06/2023
#--------------
from aritmetica import flotar, loggar
from aritmetica import velocidade_automovel
loggar('O Programa de Estruturas de Seleção foi Interpretado!')
#MAIOR VALOR
def maior_valor():
	loggar('A Função Maior Valor Iniciou')
	print('Exercício 2.1 - Maior Valor - v1'); lista = []
	print('Quantos termos deseja comparar? ',end=''); qto = flotar()
	for c in range(1, int(qto) + 1):
		print(f'Digite o Valor do {c}º Termo ',end=''); a = flotar()
		lista.append(a); a = None
	print(f'\nO maior valor desses Número é {max(lista)}')

#MENOR VALOR
def menor_valor():
	loggar('A Função Menor Valor Iniciou')
	print('Exercício 2.2 - Menor Valor'); lista = []
	print('Quantos valores deseja comparar? ',end=''); qto = flotar()
	for c in range(1 , int(qto) + 1):
		print(f'Digite o valor do {c}º Termo ',end=''); p = flotar()
		lista.append(p); p = None
		print(f'O\n Menor Termo é: {min(lista)}')

#MAIOR VALOR V2
def maior_valor_dois():
	loggar('A Função Maior Valor - V2 Iniciou')
	print('Exercício 2.3 - Maior Valor - V2');
	print('Digite dois valores abaixo') 
	a = flotar()
	b = flotar()
	#i = append(a);li
	if a == b:
		print(f'{a} é igual a {b}')
	else:
		print(f'O maior valor é {max(a, b)}')

#TERRENO GRANDE > 100
def terreno_grande():
	loggar(f'Função Terreno Grande Iniciou')
	print(f'Exercício 2.4 - Terreno Grande')
	print('Digite a a Largura do Terreno ',end=''); b = flotar()
	print('Digite o Comprimento do Terreno ',end=''); a = flotar()
	frase = 'Terreno Grande' if (a*b) > 100 else ''
	print(f'{a*b:.1f} U² (Unidades Quadradas) - {frase}\n')
	loggar(f'Fim do programa return: {a*b:.1f}')

#TERRENO GRANDE VS TERRENO PEQUENO
def terreno_grande_pequeno():
	loggar(f'Fução Terreno Grande e Pequeno Iniciou')
	print(f'Exercício 2.5 - Terreno Grande vs Terreno Pequeno')
	print('Digite a a Largura do Terreno ',end=''); b = flotar()
	print('Digite o Comprimento do Terreno ',end=''); a = flotar()
	frase = 'Terreno Grande' if (a*b) > 100 else 'Terreno Pequeno'
	print(f'{a*b:.1f} U² (Unidades Quadradas) - {frase}\n')
	loggar(f'Fim do programa return: {a*b:.1f} ')

#Maior Valor v3
def maior_valor_tres():
	loggar(f'Função Maior Valor - V3 Iniciou')
	print('Exercício 2.6 - Maior Valor - V3')
	lista, a = [], 0;
	for c in range (1, 4):
		print('Digite o valor do {c}º Termo ',end=''); p = flotar()
		lista.append(p)
	print(f'O maior valor é {max(lista)}')
	loggar(f'Fim do programa return: {max(lista)}')

#PESO IDEAL
def peso_ideal():
	loggar(f'Função Peso Ideal Iniciou')
	print('Exercício 2.7 - Peso Ideal')
	while True:
		print('Digite sua Altura em cm '); a = flotar()
		if a < 200 and a > 100:
			while True:
				print('Digite seu Peso ',end=''); p = flotar()
				if p > 40 and p < 200:
					imc = p/((a/100)**2)
					loggar(f'IMC: {imc}')
					break
				else:
					print('Peso Inválido!')
					loggar(f'Usuário Input Error - Peso')
			break
		else:
			print('Altura inválida!')
			loggar(f'Usuário Input Error - Altura')
	if imc < 18.5:
		print(f'Seu IMC está abaixo do padrão\n{imc:.2f}')
		loggar(f'Abaixo do Padrão')
	elif imc < 24.9:
		print(f'Você está no padrão,\n{imc:.2f}')
		loggar(f'No Padrão')
	elif imc < 29.9:
		print(f'Seu IMC está levemente acima do padrão.\n{imc:.2f}')
		loggar(f'Acima do Padrão')
	elif imc < 34.9:
		print(f'Você está com Obesidade Grau I.\n{imc:.2f}')
		loggar(f'Obesidade Grau I')
	elif imc < 39.9:
		print(f'Você está com Obesidade Grau II - (SEVERA).\n{imc:.2f}')
		loggar(f'Obesidade Grau II')
	elif imc >= 39.9:
		print(f'Você está com Obesidade Grau IIi - (MÓRBIDA).\n{imc:.2f}')
		loggar(f'Obesidade Grau III')
	print('\n')

#TESTE DO TRIÂNGULO
def teste_triangulo():
	loggar('Função Teste do Triângulo Iniciou')
	print('Exercício 2.8 - Teste do Triângulo')
	print('Digite o tamanho de três segmentos de reta: ')
	print('1º Seg.',end=''); s1 = flotar()
	print('2º Seg.',end=''); s2 = flotar()
	print('3º Seg.',end=''); s3 = flotar()
	if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
		print(f'É possível criar uma triângolo a partir disso.')
		loggar('Triângulo Possível')
		if s1 != s2 and s2 != s3 and s3 != s1:
			print('Esses segmentos formam um triângulo Escaleno.')
			loggar('Triângulo Escaleno')
		elif s1 == s2 == s3:
			print('Esses segmentos formam um triângulo Equilátero.')
			loggar('Triângulo Equilátero')
		else:
			print('Esses segmentos formam um Triângulo Isóceles')
			loggar('Triângulo Isóceles')
	else:
		print('Impossível criar um Triângulo')
		loggar('Triângulo Impossível')

#TESTE DO TRIÂNGULO RETÂNGULO
def triangulo_retangulo():
	loggar('Função Teste do Triângulo Retângulo Iniciou')
	print('Exercício 2.9 - Triângulo Retângulo')
	print('Digite o tamanho de três segmentos de reta: ')
	print('1º Seg.',end=''); s1 = flotar()
	print('2º Seg.',end=''); s2 = flotar()
	print('3º Seg.',end=''); s3 = flotar()
	if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
		lista = [s1, s2, s3]; hipo = max(lista); lista.remove(hipo)
		print(f'É possível criar uma triângolo a partir disso.')
		if hipo**2 == lista[0]**2 + lista[1]**2:
			print('Os valores Formam um Triângulo Retângulo!')
			loggar('Formam um Triângulo Retângulo')
		else:
			print('Os valores não formam um Triângulo Retângulo')
			loggar('Não Formam um Triângulo Retângulo')
	else:
		print('Impossível criar um Triângulo')
		loggar('Triângulo Impossível')

#FÓRMULA DE BHASKARA
def formula_bhaskara():
	loggar('Função Fórmula de Bhaskara Iniciou')
	print('Exercício 2.10 - Fórmula de Bhaskara')
	print('Entre com os coeficientes da equação abaixo ')
	print('Valor de a (ax²) ',end=''); a = flotar()
	print('Valor de b (bx) ',end=''); b = flotar()
	print('Valor de c (Termo Independente) ',end=''); c = flotar()
	delta = b**2 - 4*a*c
	if a != 0:
		if delta >= 0:
			delta = delta ** (1/2)
			x1, x2 = (b*(-1) + delta)/(2*a), (b*(-1) - delta)/(2*a)
			loggar(f'Raíz de Delta:{delta}\nX1: {x1}\nX2: {x2}')
		if delta > 0:
			print('Duas Raízes Reais e Diferentes')
			loggar(f'Duas Raízes Reais e Diferentes')
			print(f'X1 = {x1}\nX2 = {x2}')
		elif delta == 0:
			print('Duas Raízes Reais e Iguais')
			loggar('Duas Raízes Reais e Iguais')
			print(f'X1 {x1} = X2 {x2}')
		elif delta < 0:
			print('A Solução não pertence aos Reais')
			loggar('Solução não Real')
		print('\n')
	elif a == 0:
		print('O coeficientes angular a não pode ser zero em uma equação quadrática!')
		if b != 0:
			x = -c / b
			print(f'A solução dessa equação linear é {x}')
			loggar('O Usuário Digitou 0 ao coeficientes angular')
			loggar(f'Solução: {x}')
		elif c != 0:
			print('A equação não tem solução')
			loggar('Equação sem solução')
		else:
			print('Infinitas Soluções')
			loggar('Infinita Soluções')

#PESO IDEAL V2
def peso_ideal_dois():
	loggar('Função Peso Ideal - V2 Iniciou')
	print('Exercício 2.11 - Peso Ideal - V2')
	loggar("Sub-rotina Input's iniciada")
	while True:
		print('Digite sua Altura em cm '); a = flotar()
		if 200 > a > 100:
			while True:
				print('Digite seu Peso ',end=''); p = flotar()
				if 40 < p < 200:
					imc = p/((a/100)**2)
					loggar(f'Done!: {imc}')
					break
				else:
					print('Peso Inválido!')
					loggar('Usuário errou o preenchimento')
			break
		else:
			print('Altura inválida!')
			loggar('Usuário errou o preenchimento')
	lista = [19, 24, 20, 25]
	while True:
		print('Sexo\n[1] - Feminino\n[2] - Masculino'); s = flotar()
		if s == 1:
			a, b = lista[0], lista[1]; break
			loggar(f'Usuário escolheu {s}')
			loggar('Setando Valores para Mulheres')
		if s == 2:
			a, b = lista[2], lista[3]; break
			loggar(f'Usuário escolheu {s}')
			loggar('Setando Valores para Homens')
		else:
			print('Selecione 1 ou 2')
			loggar('Usuário errou o preenchimento')
	if imc < a:
		print(f'Abaixo do Peso Ideal\nIMC = {imc:.1f}')
		loggar('Abaixo do Peso')
	elif imc < b:
		print(f'Peso Ideal!. IMC = {imc:.1f}')
		loggar('Peso Ideal')
	elif imc > b:
		print(f'Acima do Peso.\nIMC = {imc:.1f}')
		loggar('Acima do Peso')
	loggar('Fim da Função Peso Ideal - V2')

#VELOCIDADE PERMITIDA
def velocidade_permitida():
	loggar('Função Velocidade Permitida Iniciou')
	print('Exercício 2.12 - Velocidade Permitida')
	ve = velocidade_automovel(); loggar(f'V: {ve}')
	if ve <= 40:
		print('Veículo Muito Lento')
		loggar('Lento')
	if ve <= 60:
		print('Veículo na velocidade permitida')
		loggar('Velocidade Permitida')
	if ve <= 80:
		print('Velocidade de cruzeiro')
		loggar('Velocidade de cruzeiro')
	if ve <= 120:
		print('Veículo rápido')
		loggar('Rápido')
	if ve > 120:
		print('Veículo muito rápido')
		loggar('Muito Rápido')
	loggar('Fim da Função Velocidade Permitida')

#ALUNO APROVADO
def aluno_aprovado():
	loggar('Função Aluno Aprovado Iniciou')
	print('Exercício 2.13 - Aluno Aprovado')
	print('Digite a AV1 ',end=''); av1 = flotar(); loggar(av1)
	print('Digite a AV2 ',end=''); av2 = flotar(); loggar(av2)
	media = (av1 + (2*av2))/3; loggar(f' Média = {media:.2f}')
	if media >= 5:
		print(f'O Aluno está APROVADO!\nMédia = {media:.2f}')
		loggar('Aprovado')
	else:
		print(f'O Aluno está REPROVADO!\nMédia = {media:.2f}')
		loggar('Reprovado')
	loggar('Fim da Função Aluno Aprovado')

