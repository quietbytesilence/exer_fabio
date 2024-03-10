#--------------
#</Gustavo Maciel>
#18/06/2023
#--------------
import math, aritmetica, estrutu_repeti, pequenos_desafios
import os, estrutu_selec, estrutu_matrizes, logging
def jogar():
	import jogo_da_velha
	jogo_da_velha
aritmetica.loggar('O Programa principal iniciou!')
#print('Olá Prof. Fábio!\nEsses são os exercícios que consegui fazer da sua lista de seleção de bolsistas\nFico a disposição para qualquer esclarecimento.')
while True:
	print('''\nEXERCÍCIOS
[1] - Aritmética Simples
[2] - Estruturas de Seleção
[3] - Estruturas de Repetição
[4] - Estruturas de Dados: Matrizes
[5] - Pequenos Desafios
[0] - Sair

Selecione o assunto do exercício através do índice.

	''')
	esc = aritmetica.intar()
	aritmetica.loggar(f'O Usuário escolheu: {esc}')
	if esc == 0:
		aritmetica.loggar('Encerrando Programa')
		logging.shutdown()
		exit()
	if esc == 1:
		print('''
Lista de Aritmética
 [0] - Voltar ao Menu
 [1] - Área do Retângulo
 [2] - Área do Quadrado
 [3] - Área do Quadradro V2
 [4] - Área do Triângulo
 [5] - Volume da Esfera
 [6] - Média Aritmética
 [7] - Média Geométrica
 [8] - Milhas vs Kilômetros
 [9] - Lei de Ohm
[10] - Celsius vs Fahrenheit
[11] - Área do Círculo
[12] - Volume do Cone
[13] - Velocidade do Automóvel
[14] - Volume do Cubo e da Esfera
[15] - Cotação do Dólar
[16] - Funções Trigonométricas
[17] - Exponencial e Logaritmo Natural
[18] - Compra e Troco
[19] - Nota para Aprovação

		   \n''')
		exe = aritmetica.intar()
		aritmetica.loggar(f'O Usuário escolheu: {esc}')
		if esc == 0:
			pass
		elif exe == 1:
			aritmetica.area_retangulo()
		elif exe == 2:
			aritmetica.area_quadrado()
		elif exe == 3:
			aritmetica.area_quadrado_dois()
		elif exe == 4:
			aritmetica.area_triangulo()
		elif exe == 5:
			aritmetica.volume_esfera()
		elif exe == 6:
			aritmetica.media_aritmetica()
		elif exe == 7:
			aritmetica.media_geometrica()
		elif exe == 8:
			aritmetica.milhas_quilometros()
		elif exe == 9:
			aritmetica.lei_ohm()
		elif exe == 10:
			aritmetica.celsius_fahrenheit()
		elif exe == 11:
			aritmetica.area_circulo()
		elif exe == 12:
		   aritmetica.volume_cone()
		elif exe == 13:
			aritmetica.velocidade_automovel()
		elif exe == 14:
			aritmetica.esfera_cubo()
		elif exe == 15:
			aritmetica.cotacao_dolar()
		elif exe == 16:
			aritmetica.trigonometricas()
		elif exe == 17:
			aritmetica.expon_loga_nat()
		elif exe == 18:
			aritmetica.compra_troco()
		elif exe == 19:
			aritmetica.nota_aprova()
		status = input('\nPRESS <ENTER> TO CONTINUE')
		os.system('cls' if os.name == 'nt' else 'clear')

	elif esc == 2:
		print('''
Lista de Estruturas de Seleção
 [0] - Voltar
 [1] - Maior Valor
 [2] - Menor Valor
 [3] - Maior Valor - V2
 [4] - Terreno Grande
 [5] - Terreno Grande vs Pequeno
 [6] - Maior Valor - V3
 [7] - Peso Ideal
 [8] - Teste do Triângulo
 [9] - Teste do Triângulo Retângulo
[10] - Fórmula de Bhaskara
[11] - Peso Ideal - V2
[12] - Velocidade Permitida
[13] - Aluno Aprovado
			''')
		esc = aritmetica.intar()
		aritmetica.loggar(f'O Usuário escolheu: {esc}')
		if esc == 0:
			pass
		if esc == 1:
			estrutu_selec.maior_valor()
		if esc == 2:
			estrutu_selec.menor_valor()
		if esc == 3:
			estrutu_selec.maior_valor_dois()
		if esc == 4:
			estrutu_selec.terreno_grande()
		if esc == 5:
			estrutu_selec.terreno_grande_pequeno()
		if esc == 6:
			estrutu_selec.maior_valor_tres()
		if esc == 7:
			estrutu_selec.peso_ideal()
		if esc == 8:
			estrutu_selec.teste_triangulo()
		if esc == 9:
			estrutu_selec.triangulo_retangulo()
		if esc == 10:
			estrutu_selec.formula_bhaskara()
		if esc == 11:
			estrutu_selec.peso_ideal_dois()
		if esc == 12:
			estrutu_selec.velocidade_permitida()
		if esc == 13:
			estrutu_selec.aluno_aprovado()
		status = input('\nPRESS <ENTER> TO CONTINUE')
		os.system('cls' if os.name == 'nt' else 'clear')
	elif esc == 3:
		print('''
Lista de Estruturas de Repetição
 [0] - Voltar
 [1] - Apenas Positivos
 [2] - Segundo Maior
 [3] - Sexo F ou M
 [4] - Tabuada do 5
 [5] - Tabuada de N Positivo
 [6] - Tabuada Parcial de um Número
 [7] - Soma de 1 a 100
 [8] - Fibonacci
 [9] - Serie de Bergamashi
[10] - N Números da Sequência - V1
[11] - N Números da Sequência - V2
[12] - N Números da Sequência - V3
[13] - Maior, Soma e Média de 3 Valores
[14] - Maior, Soma, Média e Porcentagem de N Valores - V1
[15] - Maior, Soma, Média e Porcentagem de N Valores - V2
[16] - Fatorial
			''')
		esc = aritmetica.intar()
		aritmetica.loggar(f'O Usuário escolheu: {esc}')
		if esc == 0:
			pass
		if esc == 1:
			estrutu_repeti.apena_posi()
		if esc == 2:
			estrutu_repeti.segundo_maior()
		if esc == 3:
			estrutu_repeti.sexo_f_m()
		if esc == 4:
			estrutu_repeti.tabu_cinco()
		if esc == 5:
			estrutu_repeti.tabu_dez()
		if esc == 6:
			estrutu_repeti.tabuada_parcial()
		if esc == 7:
			estrutu_repeti.sumacem()
		if esc == 8:
			estrutu_repeti.fibonacci()
		if esc == 9:
			estrutu_repeti.bergamaschi()
		if esc == 10:
			estrutu_repeti.num_seq()
		if esc == 11:
			estrutu_repeti.num_seq_dois()
		if esc == 12:
			estrutu_repeti.num_seq_tres()
		if esc == 13:
			estrutu_repeti.maior_soma_media()
		if esc == 14:
			estrutu_repeti.maior_soma_media_ad_infinitum()
		if esc == 15:
			estrutu_repeti.maior_soma_media_ad_infinitum_recursiva()
		elif esc == 16:
			estrutu_repeti.fatorial()

	elif esc == 4:
		print('''
Lista de Estruturas de Matrizes
 [0] - Voltar
 [1] - Ordem Inversa
 [2] - Produto da Matriz
 [3] - Prodtudo da Matriz - V2
 [4] - Pesquisa de Valores
 [5] - Listar Somente Mulheres
 [6] - Listar Maiores de 18
 [7] - Listar Maiores de 18 - V2
 [8] - Ordem Crescente
 [9] - Ordem Decrescente
[10] - Ordem Alfabética
[11] - Mais Novos Primeiro
			''')
		esc = aritmetica.intar()
		aritmetica.loggar(f'O Usuário escolheu: {esc}')
		if esc == 0:
			pass
		if esc == 1:
			estrutu_matrizes.inversa_ordem()
		if esc == 2:
			estrutu_matrizes.prod_matriz()
		if esc == 3:
			estrutu_matrizes.prod_matri_dois()
		if esc == 4:
			estrutu_matrizes.pesquisa_val()
		if esc == 5:
			estrutu_matrizes.somen_mulher()
		if esc == 6:
			estrutu_matrizes.somen_18()
		if esc == 7:
			estrutu_matrizes.somen_18_dois()
		if esc == 8:
			estrutu_matrizes.crece_ordem()
		if esc == 9:
			estrutu_matrizes.decresce_ordem()
		if esc == 10:
			estrutu_matrizes.alfabe_ordem()
		if esc == 11:
			estrutu_matrizes.mais_novos()
	elif esc == 5:
		print('''Pequenos Desafios
 [0] - Voltar
 [1] - Jogo da Velha
 [2] - Busca da Internet
 [3] - Tomadas Disponíveis
 [4] - Pontuação Basquete

			''')
		esc = aritmetica.intar()
		aritmetica.loggar(f'O Usuário escolheu: {esc}')
		if esc == 0:
			pass
		if esc == 1:
			jogar()
		if esc == 2:
			pequenos_desafios.num_pessoas_site()
		if esc == 3:
			pequenos_desafios.desafio_tomadas()
		if esc == 4:
			pequenos_desafios.pontu_basquete()
	else:
		print('Opção Inválida. Por favor insira um número entre 0 e 5')         
	
