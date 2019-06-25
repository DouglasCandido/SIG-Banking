# -*- coding: utf-8 -*-
# Alunos: Douglas Mateus / Lucas Eduardo
# Interface com o usuário do sistema

import os
import sys
import time
import connection
import validacao
import getpass 

running = connection.connection('root', 'douglas', 'localhost', 'bd_sig_banking')

def cabecalho():
	os.system('cls')
	print("#######################################################")
	print("##  SIG_BANKING - GERENCIADOR DE CONTAS BANCÁRIAS    ##")
	print("#######################################################")
	print("\n")

def menuCadastro():
	cabecalho()
	print("=====================================")
	print("====       C A D A S T R O       ====")
	print("=====================================")
	print()

	resposta = input("\nDeseja voltar para a Tela de Login? ")
	if(resposta != 's' and resposta != 'S'):
		pass
	elif(resposta == 's' or resposta == 'S'):
		telaLogin();

	tipo_pessoa = ''

	while(tipo_pessoa != 'F' and tipo_pessoa != 'J'):
		tipo_pessoa = input("\nVocê é Pessoa Física ou Pessoa Jurídica (F ou J)? ")
		tipo_pessoa = tipo_pessoa.upper()

	nome = input("\nNome: ")
	sobrenome = input("Sobrenome: ")

	genero = ''
	while(genero != 'H' and tipo_pessoa != "M"):
		genero = input("\nQual é o seu gênero (H - Homem ou M - Mulher)? ")
		genero = genero.upper()
	 
	email = input("\nEmail: ")
	while(validacao.validaEmail(email) == False):
		email = input("Email: ")
	
	senha = getpass.getpass("\nSenha: ")

	telefone = input("\nTelefone (Ex: (84) 99815-8089): ")
	while(validacao.validaTelefone(telefone) == False):
		telefone = input("Telefone (Ex: (84) 99815-8089): ")

	estados = ["1 - AC", "2 - AL", "3 - AP", "4 - AM", "5 - BA", "6 - CE", "7 - DF", "8 - ES", "9 - GO", "10 - MA", "11 - MT", "12 - MS", "13 - MG", "14 - PA", "15 - PB", "16 - PR", "17 - PE", "18 - PI", "19 - RJ", "20 - RN", "21 - RS", "22 - RO", "23 - RR", "24 - SC", "25 - SP", "26 - SE", "27 - TO"]
	print()
	for i in range(len(estados)):
		print(estados[i])
	uf = 0
	while(uf != 1 and uf != 2 and uf != 3 and uf != 4 and uf != 5 and uf != 6 and uf != 7 and uf != 8 and uf != 9 and uf != 10 and uf != 11 and uf != 12 and uf != 13 and uf != 14 and uf != 15 and uf != 16 and uf != 17 and uf != 18 and uf != 19 and uf != 20 and uf != 21 and uf != 22 and uf != 23 and uf != 24 and uf != 25 and uf != 26 and uf != 27):
		uf = int(input("\nDigite o número correspondente ao seu estado: "))

	cidade = input("\nCidade: ")
	bairro = input("\nBairro: ")
	rua = input("\nRua: ")
	numero_casa = input("\nNumero da casa (Ex: Apartamento 1): ")

	if(tipo_pessoa == 'F'):
		cpf = input("\nCPF (Ex: 018.308.654-63): ")
		while(validacao.validaCPF(cpf) == False):
			cpf = input("CPF (Ex: 018.308.654-63): ")
		running.add_user(tipo_pessoa, nome, sobrenome, genero, email, senha, telefone, uf, cidade, bairro, rua, numero_casa, cpf)
		print()
		print("Usuário cadastrado com sucesso!")
		time.sleep(3)
	elif(tipo_pessoa == 'J'):
		cnpj = input("\nCNPJ (Ex: 39.752.873/0005-90): ")
		while(validacao.validaCNPJ(cnpj) == False):
			cnpj = input("CNPJ (Ex: 39.752.873/0005-90): ")
		running.add_user(tipo_pessoa, nome, sobrenome, genero, email, senha, telefone, uf, cidade, bairro, rua, numero_casa, cnpj)
		print()
		print("Usuário cadastrado com sucesso!")
		time.sleep(3)

	telaLogin()

def telaNovaConta(email, senha):
	cabecalho()
	print("=====================================")
	print("====          NOVA CONTA         ====")
	print("=====================================")
	print()

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)
	else:
		pass
		
	saber_mais = input("\nDeseja saber mais sobre os tipos de contas? ")
	if(saber_mais == 's' or saber_mais == 'S'):
		print()

		print("Conta Corrente:")
		print("A conta corrente oferece acesso fácil ao seu dinheiro para suas necessidades diárias de transações, e ajuda a manter seu dinheiro seguro.")
		print("Você poderá usar cartão de crédito e débito, ou cheques para fazer compras ou pagar contas.")
		print("As contas podem ter diferentes opções ou pacotes para ajudar a evitar certas taxas de serviço mensais.")

		print()

		print("Conta Poupança:")
		print("A conta poupança permite que você acumule juros sobre fundos que você salvou para necessidades futuras.")
		print("As taxas de juros podem ser compostas em uma base diária, semanal, mensal ou anual. As contas de poupança variam de acordo com taxas de serviço mensais, taxas de juros, método usado para calcular juros e depósito mínimo de abertura.")

		print()

		print("Conta Salário:")
		print("Este tipo de conta é de exclusividade para o funcionário receber o seu salário, ela também se estende para receber 13º, PL, aposentadoria, pensão, e por ventura outros benefícios.")

		print()

		print("Conta Digital:")
		print("A conta digital é ideal para você que vive conectado, se você costuma resolver tudo on-line e muito pouco, muito pouco mesmo vai ao banco, esta é a sua conta.")
		print("Os benefícios são imensos, você ficará livre de todas as taxas e serviços cobrados pelo banco.")
		print("As suas transferências serão ilimitadas para qualquer tipo de banco, assim como os saques também são sem limites.")
		print("Todos os serviços de uma conta estão presentes na conta digital, sendo que se você precisar de algum atendimento em sua agência você poderá ser tarifado por serviço.")

		print()

		print("Conta Universitária:")
		print("O que diferencia uma conta universitária de uma conta corrente comum, é justamente o preço nos serviços que o banco poderá vim a te oferecer.")
		print("Lembrando que a Conta universitária, como o próprio nome diz é de exclusividade para estudantes de nível superior.")
		print("No geral os benefícios de uma conta universitária não variam muito de um banco para o outro, entre as listas de vantagens podemos destacar:")
		print("\tTarifas gratuitas e isenção de taxas.")
		print("\tNão tem necessidade de comprovar renda.")
		print("\tUma conta universitária te proporciona meia entrada em vários eventos, como cinema, teatro, etc.")
		print("\tCaso deseje poderá solicitar um cartão de crédito.")
		print("Para solicitar é bem fácil, vá até o seu banco de preferência com todos os seus documentos, e com os seguintes comprovantes: residência, matrícula, e da última mensalidade paga.O que diferencia uma conta universitária de uma conta corrente comum, é justamente o preço nos serviços que o banco poderá vim a te oferecer.")
	else:
		pass

	tipo_conta = ''

	while(tipo_conta != 'C' and tipo_conta != 'P' and tipo_conta != 'S' and tipo_conta != 'D' and tipo_conta != 'U'):
		tipo_conta = input("\nQual é o tipo da sua conta(C - Corrente / P - Poupança / S - Salário / D - Digital / U - Universitária)? ")
		tipo_conta = tipo_conta.upper()

	numero_conta = input("\nNúmero da conta (Ex: 123456789-1): ")
	while(validacao.validaNumeroConta(numero_conta) == False):
		numero_conta = input("\nNúmero da conta (Ex: 123456789-1): ")

	senha_conta = getpass.getpass("\nSenha: ")

	id_usuario = running.show_user_id(email, senha)

	id_banco = int(input("\nID do banco: "))

	agencia = input("\nAgência (Ex: 1234): ")
	while(validacao.validaAgencia(agencia) == False):
		agencia = input("\nAgência (Ex: 1234): ")

	running.add_account(tipo_conta, numero_conta, senha_conta, id_usuario, id_banco, agencia)
	print()
	print("Conta criada com sucesso!")
	time.sleep(3)

	menuPrincipal(email, senha)

def telaMinhasContas(email, senha):
	cabecalho()
	print("=====================================")
	print("====        MINHAS CONTAS        ====")
	print("=====================================")
	print()

	running.data_accounts(email, senha)

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaMinhasContas(email, senha) 
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def telaSaldo(email, senha):
	cabecalho()
	print("=====================================")
	print("====         MEU SALDO           ====")
	print("=====================================")
	print()

	id_conta = int(input("\nID da conta: "))

	print()

	running.ver_saldo(id_conta)

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaSaldo(email, senha) 
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def telaDeposito(email, senha):
	cabecalho()
	print("=====================================")
	print("====      DEPOSITAR DINHEIRO     ====")
	print("=====================================")
	print()

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

	id_conta = int(input("\nID da conta: "))

	senha = getpass.getpass("Senha da conta: ")

	montante = float(input("Quantidade em dinheiro (Ex: 100.00)? "))

	if(running.deposito(id_conta, senha, montante) == True):
		print("Dinheiro depositado com sucesso!")	

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaDeposito(email, senha) 
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def telaExtratoMensal(email, senha):
	cabecalho()
	print("=====================================")
	print("====        EXTRATO MENSAL       ====")
	print("=====================================")
	print()

	mes = input("\nMês desejado (Ex: Jan): ")

	running.extrato(email, senha, mes)

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaExtratoMensal(email, senha) 
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def telaLogin():
	cabecalho()
	print("=====================================")
	print("====          L O G I N          ====")
	print("=====================================")
	print()

	resposta = ''

	while(resposta != 's' and resposta != 'S' and resposta != 'n' and resposta != 'N'):
		resposta = input("Bem vindo! Você já possui cadastro no nosso sistema? ")
		print()

	if(resposta == 's' or resposta == 'S'):

		email = input("Email: ")
		while(validacao.validaEmail(email) == False):
			email = input("Email: ")
		senha = getpass.getpass("Senha: ")

		if(running.login(email, senha) == True):
			menuPrincipal(email, senha)
		else:
			print("\nOs dados informados estão incorretos.")
			print("\nRedirecionando...")
			time.sleep(3)
			telaLogin()

	else:
		menuCadastro()

def telaMeusDados(email, senha):
	cabecalho()
	print("=====================================")
	print("====     MEUS DADOS PESSOAIS     ====")
	print("=====================================")
	print()

	running.data_user(email, senha)

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaMeusDados(email, senha) 
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def telaVerBancos(email, senha):
	cabecalho()
	print("==================================================")
	print("====   BANCOS CADASTRADOS NO NOSSO SISTEMA    ====")
	print("==================================================")
	print()

	running.ver_bancos()

	resposta = input("\nDeseja voltar para o Menu Principal? ")
	while(resposta != 's' and resposta != 'S'):
		telaVerBancos(email, senha)
		resposta = input("\nDeseja voltar para o Menu Principal? ")
	if(resposta == 's' or resposta == 'S'):
		menuPrincipal(email, senha)

def menuPrincipal(email, senha):
	cabecalho()

	running.introduce_user_name(email, senha)

	print("=====================================")
	print("==== M E N U   P R I N C I P A L ====")
	print("=====================================")
	print()
	print("\t1 - Meus dados")
	print("\t2 - Minhas contas")
	print("\t3 - Cadastrar nova conta")
	print("\t4 - Saldo")
	print("\t5 - Deposito")
	print("\t6 - Histórico de transações")
	print("\t7 - Ver bancos cadastrados no sistema")
	print("\t0 - Finalizar Programa")
	print()
	print("=====================================")
	print()

	op = int(input("Escolha sua opção: "))
	while(op != 0 and op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op != 7):
  		op = input("Escolha sua opção: ")

	if(op == 0):
		print("\nObrigado por usar o Sig_Banking, tenha um bom dia.")
		sys.exit(0)
	elif(op == 1):
		telaMeusDados(email, senha)
	elif(op == 2):
		telaMinhasContas(email, senha)
	elif(op == 3):
		telaNovaConta(email, senha)
	elif(op == 4):
		telaSaldo(email, senha)
	elif(op == 5):
		telaDeposito(email, senha)
	elif(op == 6):
		telaExtratoMensal(email, senha)
	elif(op == 7):
		telaVerBancos(email, senha)

# A tela de login é a tela inicial do sistema, a partir dela, outras serão invocadas.
telaLogin()