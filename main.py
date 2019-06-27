# -*- coding: utf-8 -*-
# Alunos: Douglas Mateus / Lucas Eduardo
# Interface com o usuário do sistema

import os
import sys
import time
import connection
import validacao
import getpass
import validate_email

running = connection.connection(
    'root', 'douglas', 'localhost', 'bd_sig_banking')


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
        telaLogin()

    tipo_pessoa = ''

    while(tipo_pessoa != 'F' and tipo_pessoa != 'J'):
        tipo_pessoa = input(
            "\nVocê é Pessoa Física ou Pessoa Jurídica (F ou J)? ")
        tipo_pessoa = tipo_pessoa.upper()

    nome = input("\nNome: ")
    sobrenome = input("Sobrenome: ")

    genero = ''
    while(genero != 'H' and tipo_pessoa != "M"):
        genero = input("\nQual é o seu gênero (H - Homem ou M - Mulher)? ")
        genero = genero.upper()

    email = input("\nEmail: ")
    while(validacao.validaEmail(email) == False):
        email = input("\nEmail: ")

    while(running.integridade_email(email) == False):
            email = input("\nEmail: ")

    senha = getpass.getpass("\nSenha: ")

    telefone = input("\nTelefone (Ex: (84) 99815-8089): ")
    while(validacao.validaTelefone(telefone) == False):
        telefone = input("Telefone (Ex: (84) 99815-8089): ")

    estados = ["1 - AC", "2 - AL", "3 - AP", "4 - AM", "5 - BA", "6 - CE", "7 - DF", "8 - ES", "9 - GO", "10 - MA", "11 - MT", "12 - MS", "13 - MG",
               "14 - PA", "15 - PB", "16 - PR", "17 - PE", "18 - PI", "19 - RJ", "20 - RN", "21 - RS", "22 - RO", "23 - RR", "24 - SC", "25 - SP", "26 - SE", "27 - TO"]
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

        while(running.integridade_cpf(cpf) == False):
            cpf = input("CPF (Ex: 018.308.654-63): ")

        running.add_user(tipo_pessoa, nome, sobrenome, genero, email,
                             senha, telefone, uf, cidade, bairro, rua, numero_casa, cpf)
        print()
        print("\nUsuário cadastrado com sucesso!")
        time.sleep(3)

    elif(tipo_pessoa == 'J'):

        cnpj = input("\nCNPJ (Ex: 39.752.873/0005-90): ")
        while(validacao.validaCNPJ(cnpj) == False):
            cnpj = input("CNPJ (Ex: 39.752.873/0005-90): ")

        while(running.integridade_cnpj(cnpj) == False):
            cnpj = input("CNPJ (Ex: 39.752.873/0005-90): ")

        running.add_user(tipo_pessoa, nome, sobrenome, genero, email,
                         senha, telefone, uf, cidade, bairro, rua, numero_casa, cnpj)
        print()
        print("\nUsuário cadastrado com sucesso!")
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
        tipo_conta = input(
            "\nQual é o tipo da sua conta(C - Corrente / P - Poupança / S - Salário / D - Digital / U - Universitária)? ")
        tipo_conta = tipo_conta.upper()

    numero_conta = input("\nNúmero da conta (Ex: 123456789-1): ")
    while(validacao.validaNumeroConta(numero_conta) == False):
        numero_conta = input("\nNúmero da conta (Ex: 123456789-1): ")

    while(running.integridade_numero_conta(numero_conta) == False):
        numero_conta = input("\nNúmero da conta (Ex: 123456789-1): ")        

    senha_conta = getpass.getpass("\nSenha: ")

    id_usuario = running.show_user_id(email, senha)

    id_banco = int(input("\nID do banco: "))
    while(running.integridade_banco(id_banco) == False):
            id_banco = int(input("\nID do banco: "))

    agencia = input("\nAgência (Ex: 1234): ")
    while(validacao.validaAgencia(agencia) == False):
        agencia = input("\nAgência (Ex: 1234): ")

    running.add_account(tipo_conta, numero_conta,
                        senha_conta, id_usuario, id_banco, agencia)
    print()
    print("\nConta criada com sucesso!")
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

    senha = getpass.getpass("\nSenha da conta: ")

    montante = float(input("\nQuantidade em dinheiro (Ex: 100.00)? "))

    if(running.deposito(id_conta, senha, montante) == True):
        print("\nDinheiro depositado com sucesso!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaDeposito(email, senha)
        resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

def telaSaque(email, senha):
    cabecalho()
    print("=====================================")
    print("====      SACAR DINHEIRO         ====")
    print("=====================================")
    print()

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

    id_conta = int(input("\nID da conta: "))

    senha = getpass.getpass("\nSenha da conta: ")

    montante = float(input("\nQuantidade em dinheiro (Ex: 100.00)? "))

    if(running.saque(id_conta, senha, montante) == True):
        print("\nDinheiro sacado com sucesso!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaSaque(email, senha)
        resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

def telaTransferencia(email, senha):
    cabecalho()
    print("=====================================")
    print("====     TRANSFERIR DINHEIRO     ====")
    print("=====================================")
    print()

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

    numero_conta_origem = input("\nNúmero da conta de orígem (Sua conta): ")
    while(validacao.validaNumeroConta(numero_conta_origem) == False):
        numero_conta_origem = input("\nNúmero da conta de orígem (Sua conta): ")

    senha_conta_origem = getpass.getpass("\nSenha da conta: ")

    numero_conta_destino = input("\nNúmero da conta de destino: ")
    while(validacao.validaNumeroConta(numero_conta_destino) == False):
        numero_conta_destino = input("\nNúmero da conta de destino: ")

    while(numero_conta_destino == numero_conta_origem):
        numero_conta_destino = input("\nNúmeros das contas são iguais. Digite novamente um número, diferente, da conta de destino: ")

    montante_origem = float(input("\nQuantidade em dinheiro (Ex: 100.00)? "))

    if(running.transferencia(numero_conta_origem, senha_conta_origem, numero_conta_destino, montante_origem) == True):
        print("\nTransferência bem sucedida!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaTransferencia(email, senha)
        resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)


def telaExtratoMensal(email, senha):
    cabecalho()
    print("=====================================")
    print("====        EXTRATO MENSAL       ====")
    print("=====================================")
    print()

    mes = input("\nMês desejado (Ex: Jun): ")
    ano = input("\nAno desejado (Ex: 2019): ")

    running.extrato(email, senha, mes, ano)

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

def telaAlterarConta(email, senha):
    cabecalho()
    print("==================================================")
    print("====        MODIFICAR DADOS DA CONTA          ====")
    print("==================================================")
    print()

    print("\nAtributos que podem ser alterados: Tipo da conta e senha.")

    id_conta = int(input("\nDigite o ID da conta que será modificada: "))

    r1 = input("\nDeseja alterar o tipo da sua conta? ")
    if(r1.upper() == 'S'):
        tipo_conta = input("\nQual é o tipo da sua conta(C - Corrente / P - Poupança / S - Salário / D - Digital / U - Universitária)? ")
        while(tipo_conta != 'C' and tipo_conta != 'P' and tipo_conta != 'S' and tipo_conta != 'D' and tipo_conta != 'U'):
            tipo_conta = input("\nQual é o tipo da sua conta(C - Corrente / P - Poupança / S - Salário / D - Digital / U - Universitária)? ")
        tipo_conta = tipo_conta.upper()
        if(running.alterar_conta_tc(email, senha, id_conta, tipo_conta) == True):
            print("\nO tipo da conta foi alterado!")

    r2 = input("\nDeseja alterar a senha da sua conta? ")
    if(r2.upper() == 'S'):
        senha_conta = getpass.getpass("\nNova senha: ")
        if(running.alterar_conta_senha(email, senha, id_conta, senha_conta) == True):
            print("\nA senha da conta foi alterada!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaAlterarConta(email, senha)
        resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

def telaAlterarDadosPessoais(email, senha):
    cabecalho()
    print("==================================================")
    print("====        MODIFICAR DADOS PESSOAIS          ====")
    print("==================================================")
    print()

    print("\nAtributos que podem ser alterados: Nome, Sobrenome, Email, Senha, Telefone, Estado, Cidade, Bairro, Rua, Número da casa.")

    r1 = input("\nDeseja alterar o seu nome? ")
    if(r1.upper() == 'S'):
        nome = input("\n Digite o seu novo nome: ")
        if(running.alterar_usuario_nome(email, senha, nome) == True):
            print("\nO seu nome foi alterado!")

    r2 = input("\nDeseja alterar o seu sobrenome? ")
    if(r2.upper() == 'S'):
        sobrenome = input("\nDigite o seu novo sobrenome: ")
        if(running.alterar_usuario_sobrenome(email, senha, sobrenome) == True):
            print("\nO seu sobrenome foi alterado!")

    r3 = input("\nDeseja alterar o seu email? ")
    if(r3.upper() == 'S'):
        novo_email = input("\nEmail: ")
        while(validacao.validaEmail(email) == False):
            novo_email = input("\nEmail: ")
        if(running.alterar_usuario_email(email, senha, novo_email) == True):
            print("\nO seu email foi alterado!")
            email = novo_email

    r4 = input("\nDeseja alterar a sua senha? ")
    if(r4.upper() == 'S'):
        nova_senha = getpass.getpass("Nova senha: ")
        if(running.alterar_usuario_senha(email, senha, nova_senha) == True):
            print("\nA sua senha foi alterada!")
            senha = nova_senha

    r5 = input("\nDeseja alterar o seu telefone? ")
    if(r5.upper() == 'S'):
        telefone = input("\nTelefone: ")
        while(validacao.validaTelefone(telefone) == False):
            telefone = input("\nTelefone: ")
        if(running.alterar_usuario_telefone(email, senha, telefone) == True):
            print("\nO seu telefone foi alterado!")

    # Endereço
    r6 = input("\nDeseja alterar o seu estado (Unidade Federal)? ")
    if(r6.upper() == 'S'):

        estados = ["1 - AC", "2 - AL", "3 - AP", "4 - AM", "5 - BA", "6 - CE", "7 - DF", "8 - ES", "9 - GO", "10 - MA", "11 - MT", "12 - MS", "13 - MG",
               "14 - PA", "15 - PB", "16 - PR", "17 - PE", "18 - PI", "19 - RJ", "20 - RN", "21 - RS", "22 - RO", "23 - RR", "24 - SC", "25 - SP", "26 - SE", "27 - TO"]
        print()

        for i in range(len(estados)):
            print(estados[i])

        uf = 0
        while(uf != 1 and uf != 2 and uf != 3 and uf != 4 and uf != 5 and uf != 6 and uf != 7 and uf != 8 and uf != 9 and uf != 10 and uf != 11 and uf != 12 and uf != 13 and uf != 14 and uf != 15 and uf != 16 and uf != 17 and uf != 18 and uf != 19 and uf != 20 and uf != 21 and uf != 22 and uf != 23 and uf != 24 and uf != 25 and uf != 26 and uf != 27):
            uf = int(input("\nDigite o número correspondente ao seu estado: "))

        if(running.alterar_usuario_estado(email, senha, uf) == True):
            print("\nO seu estado foi alterado!")

    r7 = input("\nDeseja alterar a sua cidade? ")
    if(r7.upper() == 'S'):
        cidade = input("\nCidade: ")
        if(running.alterar_usuario_cidade(email, senha, cidade) == True):
            print("\nA sua cidade foi alterada!")

    r8 = input("\nDeseja alterar o seu bairro? ")
    if(r8.upper() == 'S'):
        bairro = input("\nBairro: ")
        if(running.alterar_usuario_bairro(email, senha, bairro) == True):
            print("\nO seu bairro foi alterado!")

    r9 = input("\nDeseja alterar a sua rua? ")
    if(r9.upper() == 'S'):
        rua = input("\nRua: ")
        if(running.alterar_usuario_rua(email, senha, rua) == True):
            print("\nA sua rua foi alterada!")

    r10 = input("\nDeseja alterar o seu número de residência? ")
    if(r10.upper() == 'S'):
        numero_casa = input("\nNúmero da residência: ")
        if(running.alterar_usuario_numero_casa(email, senha, numero_casa) == True):
            print("\nO seu número de residência foi alterado!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaAlterarConta(email, senha)
        resposta = input("\nDeseja voltar para o Menu Principal? ")
    if(resposta == 's' or resposta == 'S'):
        menuPrincipal(email, senha)

def telaEncerrarConta(email, senha):
    cabecalho()
    print("==================================================")
    print("====          ENCERRAMENTO DE CONTA           ====")
    print("==================================================")
    print()

    print("\nCuidado para não ter arrependimentos. Encerrar uma conta não pode ser desfeito.")

    id_conta = int(input("\nDigite o ID da conta que será encerrada: "))

    if(running.encerrar_conta(email, senha, id_conta) == True):
        print("\nConta encerrada!")

    resposta = input("\nDeseja voltar para o Menu Principal? ")
    while(resposta != 's' and resposta != 'S'):
        telaEncerrarConta(email, senha)
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
    print("1 - Meus dados")
    print("2 - Minhas contas")
    print("3 - Cadastrar nova conta")
    print("4 - Saldo")
    print("5 - Deposito")
    print("6 - Histórico de transações")
    print("7 - Ver bancos cadastrados no sistema")
    print("8 - Saque")
    print("9 - Transferência")
    print("10 - Alterar dados pessoais")
    print("11 - Alterar dados das contas")
    print("12 - Encerrar conta")
    print("0 - Sair do sistema")
    print()
    print("=====================================")
    print()

    op = int(input("Escolha sua opção: "))
    while(op != 0 and op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op != 7 and op != 8 and op != 9 and op != 10 and op != 11 and op != 12):
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
    elif(op == 8):
        telaSaque(email, senha)
    elif(op == 9):
        telaTransferencia(email, senha)
    elif(op == 10):
        telaAlterarDadosPessoais(email, senha)
    elif(op == 11):
        telaAlterarConta(email, senha)
    elif(op == 12):
        telaEncerrarConta(email, senha)

# A tela de login é a tela inicial do sistema, a partir dela, outras serão invocadas.
telaLogin()
