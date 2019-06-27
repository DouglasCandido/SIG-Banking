import sys
import datetime

# Conexão com o BD ###############################################################################################
try:
    import mysql.connector
except ImportError as e:
    print(e)


class connection:

    def __init__(self, user, password, host, db):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__db = db

        try:
            self.__conn = mysql.connector.connect(
                user=self.__user, password=self.__password, host=self.__host, database=self.__db)
            self.__cursor = self.__conn.cursor()
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.__conn.close()

    # Cadastra um usuário
    def add_user(self, tipo_pessoa, nome, sobrenome, genero, email, senha, telefone, uf, cidade, bairro, rua, numero_casa, cpf=None, cnpj=None):

        self.__tipo_pessoa = tipo_pessoa
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__genero = genero
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero_casa = numero_casa
        self.__cpf = cpf
        self.__cnpj = cnpj

        data_tempo_atual = datetime.datetime.now()
        self.__data_de_cadastro = data_tempo_atual.strftime(
            "%d/%b/%Y (%H:%M:%S)")

        query_add_user = """INSERT INTO Usuario (tipo_pessoa, nome, sobrenome, genero, email, senha, telefone, id_uf, cidade, bairro, rua, numero_casa, cpf, cnpj, data_de_cadastro) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', {7}, '{8}', '{9}', 
        '{10}', '{11}',  '{12}',  '{13}',  '{14}')""".format(self.__tipo_pessoa, self.__nome,
                                                             self.__sobrenome, self.__genero, self.__email, self.__senha, self.__telefone, self.__uf, self.__cidade,
                                                             self.__bairro, self.__rua, self.__numero_casa, self.__cpf, self.__cnpj, self.__data_de_cadastro)

        try:
            self.__cursor.execute(query_add_user)
            self.__conn.commit()

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def encerrar_conta(self, email, senha, id_conta):

        self.__email = email
        self.__senha = senha
        self.__id_conta = id_conta

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]
            query_encerrar_deposito = ("DELETE FROM Deposito WHERE id_conta = {0}".format(self.__id_conta))
            self.__cursor.execute(query_encerrar_deposito)
            query_encerrar_saque = ("DELETE FROM Saque WHERE id_conta = {0}".format(self.__id_conta))
            self.__cursor.execute(query_encerrar_saque)
            query_encerrar_transferencia = ("DELETE FROM Transferencia WHERE id_conta_origem = {0}".format(self.__id_conta))
            self.__cursor.execute(query_encerrar_transferencia)
            query_encerrar_saldo = ("DELETE FROM Conta WHERE id = {0}".format(self.__id_conta))
            self.__cursor.execute(query_encerrar_saldo)
            query_encerrar_conta = ("DELETE FROM Conta WHERE id = {0} and id_usuario = {1}".format(self.__id_conta, self.__id_usuario))

        try:
            self.__cursor.execute(query_encerrar_conta)
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_conta_tc(self, email, senha, id_conta, tipo_conta):

        self.__email = email
        self.__senha = senha
        self.__id_conta = id_conta
        self.__tipo_conta = tipo_conta

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Conta SET tipo_conta = %s WHERE id = %s and id_usuario = %s;", (self.__tipo_conta, str(self.__id_conta), str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_conta_senha(self, email, senha, id_conta, senha_conta):

        self.__email = email
        self.__senha = senha
        self.__id_conta = id_conta
        self.__senha_conta = senha_conta

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Conta SET senha = %s WHERE id = %s and id_usuario = %s;", (self.__senha_conta, str(self.__id_conta), str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_nome(self, email, senha, nome):

        self.__email = email
        self.__senha = senha

        self.__nome = nome

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET nome = %s WHERE id = %s;", (self.__nome, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_sobrenome(self, email, senha, sobrenome):

        self.__email = email
        self.__senha = senha

        self.__sobrenome = sobrenome

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET sobrenome = %s WHERE id = %s;", (self.__sobrenome, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_email(self, email, senha, novo_email):

        self.__email = email
        self.__senha = senha

        self.__novo_email = novo_email

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET email = %s WHERE id = %s;", (self.__novo_email, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_senha(self, email, senha, nova_senha):

        self.__email = email
        self.__senha = senha

        self.__nova_senha = nova_senha

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET senha = %s WHERE id = %s;", (self.__nova_senha, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_telefone(self, email, senha, telefone):

        self.__email = email
        self.__senha = senha

        self.__telefone = telefone

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET telefone = %s WHERE id = %s;", (self.__telefone, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_estado(self, email, senha, id_uf):

        self.__email = email
        self.__senha = senha

        self.__id_uf = id_uf

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET id_uf = %s WHERE id = %s;", (str(self.__id_uf), str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_cidade(self, email, senha, cidade):

        self.__email = email
        self.__senha = senha

        self.__cidade = cidade

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET cidade = %s WHERE id = %s;", (self.__cidade, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_bairro(self, email, senha, bairro):

        self.__email = email
        self.__senha = senha

        self.__bairro = bairro

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET bairro = %s WHERE id = %s;", (self.__bairro, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_rua(self, email, senha, rua):

        self.__email = email
        self.__senha = senha

        self.__rua = rua

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET rua = %s WHERE id = %s;", (self.__rua, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def alterar_usuario_numero_casa(self, email, senha, numero_casa):

        self.__email = email
        self.__senha = senha

        self.__numero_casa = numero_casa

        query_usuario = ("SELECT * FROM Usuario WHERE email = '{0}' and senha = '{1}'".format(self.__email, self.__senha))
        self.__cursor.execute(query_usuario)        
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        try:
            self.__cursor.execute("UPDATE Usuario SET numero_casa = %s WHERE id = %s;", (self.__numero_casa, str(self.__id_usuario)))
            self.__conn.commit()
            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def integridade_cpf(self, cpf):

        self.__cpf = cpf

        query_verificadora = ("SELECT * FROM Usuario WHERE cpf = '{x1}'".format(x1 = self.__cpf))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    def integridade_cnpj(self, cnpj):

        self.__cnpj = cnpj

        query_verificadora = ("SELECT * FROM Usuario WHERE cnpj = '{x1}'".format(x1 = self.__cnpj))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    def integridade_email(self, email):

        self.__email = email

        query_verificadora = ("SELECT * FROM Usuario WHERE email = '{x1}'".format(x1 = self.__email))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    # Valida o login no sistema
    def login(self, email, senha):

        self.__email = email
        self.__senha = senha

        try:

            self.__cursor.execute(
                "SELECT * FROM Usuario WHERE email = %s AND senha = %s;", (self.__email, self.__senha))

            result = self.__cursor.fetchone()

            if(result == None):
                return False
            else:
                return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Mostra o nome do usuário, é utilizado apenas para dar boas vindas
    def introduce_user_name(self, email, senha):

        self.__email = email
        self.__senha = senha

        try:

            self.__cursor.execute(
                "SELECT * FROM Usuario WHERE email = %s AND senha = %s;", (self.__email, self.__senha))

            result = self.__cursor.fetchone()

            if(result == None):
                return False
            else:
                print("Bem vindo, %s.\n" % result[2])

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Mostra o id do usuário, é utilizado como chave estrangeira em algumas tabelas
    def show_user_id(self, email, senha):

        self.__email = email
        self.__senha = senha

        try:

            self.__cursor.execute(
                "SELECT * FROM Usuario WHERE email = %s AND senha = %s;", (self.__email, self.__senha))

            result = self.__cursor.fetchone()

            if(result == None):
                return False
            else:
                return result[0]

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Recupera todos os dados do usuário
    def data_user(self, email, senha):

        self.__email = email
        self.__senha = senha

        try:
            self.__cursor.execute(
                "SELECT * FROM Usuario WHERE email = %s AND senha = %s;", (self.__email, self.__senha))
            result_valores = self.__cursor.fetchone()

            if(result_valores == None):
                return False

            else:
                for i in range(len(result_valores)):
                    if(i == 0):
                        # nome_coluna = 'ID'
                        # print("%s: %s" %(nome_coluna, result_valores[0]))
                        pass
                    elif(i == 1):
                        nome_coluna = 'Tipo de Pessoa'
                        print("%s: %s" % (nome_coluna, result_valores[1]))
                    elif(i == 2):
                        nome_coluna = 'Nome'
                        print("%s: %s" % (nome_coluna, result_valores[2]))
                    elif(i == 3):
                        nome_coluna = 'Sobrenome'
                        print("%s: %s" % (nome_coluna, result_valores[3]))
                    elif(i == 4):
                        nome_coluna = 'Gênero'
                        print("%s: %s" % (nome_coluna, result_valores[4]))
                    elif(i == 5):
                        nome_coluna = 'Email'
                        print("%s: %s" % (nome_coluna, result_valores[5]))
                    elif(i == 6):
                        nome_coluna = 'Senha'
                        print("%s: %s" % (nome_coluna, result_valores[6]))
                    elif(i == 7):
                        nome_coluna = 'Telefone'
                        print("%s: %s" % (nome_coluna, result_valores[7]))
                    elif(i == 8):

                        self.__cursor.execute(
                            "SELECT nome FROM Uf WHERE id = " + str(result_valores[8]))
                        result_nome_estado = self.__cursor.fetchone()

                        if(result_nome_estado == None):
                            pass
                        else:
                            nome_estado = result_nome_estado[0]
                        nome_coluna = 'Estado'
                        print("%s: %s" % (nome_coluna, nome_estado))

                    elif(i == 9):
                        nome_coluna = 'Cidade'
                        print("%s: %s" % (nome_coluna, result_valores[9]))
                    elif(i == 10):
                        nome_coluna = 'Bairro'
                        print("%s: %s" % (nome_coluna, result_valores[10]))
                    elif(i == 11):
                        nome_coluna = 'Rua'
                        print("%s: %s" % (nome_coluna, result_valores[11]))
                    elif(i == 12):
                        nome_coluna = 'Número da casa'
                        print("%s: %s" % (nome_coluna, result_valores[12]))
                    elif(i == 13):
                        nome_coluna = 'CPF'
                        print("%s: %s" % (nome_coluna, result_valores[13]))
                    elif(i == 14):
                        #nome_coluna = 'CNPJ'
                        #print("%s: %s" %(nome_coluna, result_valores[14]))
                        pass
                    elif(i == 15):
                        nome_coluna = 'Data de Cadastro'
                        print("%s: %s" % (nome_coluna, result_valores[15]))

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Adiciona um banco
    def add_bank(self, cnpj, nome, email):

        self.__cnpj = cnpj
        self.__nome = nome
        self.__email = email
        # self.__telefone = telefone

        query_add_bank = """INSERT INTO Banco (cnpj, nome, email) VALUES ('{0}', '{1}', '{2}')""".format(
            self.__cnpj, self.__nome, self.__email)

        try:
            self.__cursor.execute(query_add_bank)
            self.__conn.commit()
        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def integridade_banco(self, id_banco):

        self.__id_banco = id_banco

        query_verificadora = ("SELECT * FROM Banco WHERE id = {x1}".format(x1 = self.__id_banco))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return False
        else:
            return True

    def integridade_cnpj_banco(self, cnpj):

        self.__cnpj = cnpj

        query_verificadora = ("SELECT * FROM Banco WHERE cnpj = '{x1}'".format(x1 = self.__cnpj))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    def integridade_email_banco(self, email):

        self.__email = email

        query_verificadora = ("SELECT * FROM Banco WHERE email = '{x1}'".format(x1 = self.__email))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    def integridade_nome_banco(self, nome):

        self.__nome = nome

        query_verificadora = ("SELECT * FROM Banco WHERE nome = '{x1}'".format(x1 = self.__nome))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    # Carrega a lista de bancos cadastrados no sistema
    def ver_bancos(self):

        query_ver_bancos = "SELECT * FROM Banco;"

        try:
            self.__cursor.execute(query_ver_bancos)

            bancos = self.__cursor.fetchall()

            for banco in bancos:
                for i in range(len(banco)):
                    if(i == 0):
                        nome_coluna = "ID do banco"
                        print("%s: %s" % (nome_coluna, banco[0]))
                    elif(i == 1):
                        nome_coluna = "CNPJ"
                        print("%s: %s" % (nome_coluna, banco[1]))
                    elif(i == 2):
                        nome_coluna = "Nome"
                        print("%s: %s" % (nome_coluna, banco[2]))
                    elif(i == 3):
                        nome_coluna = "Email"
                        print("%s: %s" % (nome_coluna, banco[3]))
                print("---------------------------------")
                print()

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    # Mostra o saldo atual de uma conta
    def ver_saldo(self, id_conta):

        self.__id_conta = id_conta

        query_ver_saldo = "SELECT * FROM Conta where id = " + \
            str(self.__id_conta)

        try:
            self.__cursor.execute(query_ver_saldo)

            conta = self.__cursor.fetchall()

            for coluna in conta:
                for i in range(len(coluna)):
                    if(i == 0):
                        pass
                    elif(i == 1):
                        nome_coluna = "Tipo da conta"
                        print("%s: %s" % (nome_coluna, coluna[1]))
                    elif(i == 2):
                        nome_coluna = "Número da conta"
                        print("%s: %s" % (nome_coluna, coluna[2]))
                    elif(i == 3):
                        pass
                    elif(i == 4):
                        self.__cursor.execute(
                            "SELECT nome FROM Usuario WHERE id = " + str(coluna[4]))
                        result_nome_usuario = self.__cursor.fetchone()

                        if(result_nome_usuario == None):
                            pass
                        else:
                            nome_usuario = result_nome_usuario[0]
                        nome_coluna = "Dono da conta"
                        print("%s: %s" % (nome_coluna, nome_usuario))
                    elif(i == 5):
                        self.__cursor.execute(
                            "SELECT nome FROM Banco WHERE id = " + str(coluna[5]))
                        result_nome_banco = self.__cursor.fetchone()

                        if(result_nome_banco == None):
                            pass
                        else:
                            nome_banco = result_nome_banco[0]
                        nome_coluna = "Banco"
                        print("%s: %s" % (nome_coluna, nome_banco))
                    elif(i == 6):
                        nome_coluna = "Agência"
                        print("%s: %s" % (nome_coluna, coluna[6]))
                    elif(i == 7):
                        self.__montante = "R$ " + str(coluna[7])
                        nome_coluna = "Montante"
                        print("%s: %s" % (nome_coluna, self.__montante))
                    elif(i == 8):
                        nome_coluna = "Data Atual"
                        data_tempo_atual = datetime.datetime.now()
                        self.__data_da_operacao = data_tempo_atual.strftime(
                            "%d/%b/%Y (%H:%M:%S)")
                        print("%s: %s" % (nome_coluna, self.__data_da_operacao))
                print("---------------------------------")
                print()

            query_registrar_saldo = """INSERT INTO Saldo (id_conta, montante_na_data_da_operacao, data_da_operacao) VALUES ({0}, '{1}', '{2}')""".format(
                self.__id_conta, self.__montante, self.__data_da_operacao)
            self.__cursor.execute(query_registrar_saldo)
            self.__conn.commit()

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    # Mostra todas as operações realizadas pelo usuário em um determinado mês
    def extrato(self, email, senha, mes, ano):

        self.__email = email
        self.__senha = senha

        self.__cursor.execute(
            "SELECT * FROM Usuario WHERE email = %s AND senha = %s;", (self.__email, self.__senha))
        result_usuario = self.__cursor.fetchone()

        if(result_usuario == None):
            return False
        else:
            self.__id_usuario = result_usuario[0]

        query_conta = "SELECT * FROM Conta WHERE id_usuario = " + \
            str(self.__id_usuario)
        self.__cursor.execute(query_conta)

        result_conta = self.__cursor.fetchall()

        if(result_conta == None):
            return False
        else:

            print("\n* Registros de checagens de saldos no mês e ano informados:")
            print()
            for conta in result_conta:
                self.__id_conta = conta[0]
                query_saldo = "SELECT * FROM Saldo WHERE id_conta = " + \
                    str(self.__id_conta)
                self.__cursor.execute(query_saldo)

                result_saldo = self.__cursor.fetchall()

                for x in result_saldo:
                    data_dividida_em_partes = x[3].split('/')
                    mes_armazenado = data_dividida_em_partes[1]
                    nova_data_dividida_em_partes = data_dividida_em_partes[2]
                    nova_data_dividida_em_partes = nova_data_dividida_em_partes.split(
                        ' ')
                    ano_armazenado = nova_data_dividida_em_partes[0]
                    if(mes == mes_armazenado and ano == ano_armazenado):
                        for i in range(len(x)):
                            if(i == 0):
                                pass
                            elif(i == 1):
                                pass
                            elif(i == 2):
                                nome_coluna = "Número da conta"
                                print("%s: %s" % (nome_coluna, conta[2]))
                                nome_coluna = "Montante na data da operação"
                                print("%s: %s" % (nome_coluna, x[2]))
                            elif(i == 3):
                                nome_coluna = "Data da operação"
                                print("%s: %s" % (nome_coluna, x[3]))
                        print("---------------------------------")
                        print()

            print("\n* Registros de depósitos no mês e ano informados:")
            print()
            for conta in result_conta:
                self.__id_conta = conta[0]
                query_deposito = "SELECT * FROM Deposito WHERE id_conta = " + \
                    str(self.__id_conta)
                self.__cursor.execute(query_deposito)

                result_deposito = self.__cursor.fetchall()

                for y in result_deposito:
                    data_dividida_em_partes = y[3].split('/')
                    mes_armazenado = data_dividida_em_partes[1]
                    nova_data_dividida_em_partes = data_dividida_em_partes[2]
                    nova_data_dividida_em_partes = nova_data_dividida_em_partes.split(
                        ' ')
                    ano_armazenado = nova_data_dividida_em_partes[0]
                    if(mes == mes_armazenado and ano == ano_armazenado):
                        for i in range(len(y)):
                            if(i == 0):
                                pass
                            elif(i == 1):
                                pass
                            elif(i == 2):
                                nome_coluna = "Número da conta"
                                print("%s: %s" % (nome_coluna, conta[2]))
                                nome_coluna = "Montante depositado"
                                print("%s: %s" % (nome_coluna, y[2]))
                            elif(i == 3):
                                nome_coluna = "Data da operação"
                                print("%s: %s" % (nome_coluna, y[3]))
                        print("---------------------------------")
                        print()

            print("\n* Registros de saques no mês e ano informados:")
            print()
            for conta in result_conta:
                self.__id_conta = conta[0]
                query_saque = "SELECT * FROM Saque WHERE id_conta = " + \
                    str(self.__id_conta)
                self.__cursor.execute(query_saque)

                result_saque = self.__cursor.fetchall()

                for z in result_saque:
                    data_dividida_em_partes = z[3].split('/')
                    mes_armazenado = data_dividida_em_partes[1]
                    nova_data_dividida_em_partes = data_dividida_em_partes[2]
                    nova_data_dividida_em_partes = nova_data_dividida_em_partes.split(
                        ' ')
                    ano_armazenado = nova_data_dividida_em_partes[0]
                    if(mes == mes_armazenado and ano == ano_armazenado):
                        for i in range(len(y)):
                            if(i == 0):
                                pass
                            elif(i == 1):
                                pass
                            elif(i == 2):
                                nome_coluna = "Número da conta"
                                print("%s: %s" % (nome_coluna, conta[2]))
                                nome_coluna = "Montante sacado"
                                print("%s: %s" % (nome_coluna, z[2]))
                            elif(i == 3):
                                nome_coluna = "Data da operação"
                                print("%s: %s" % (nome_coluna, z[3]))
                        print("---------------------------------")
                        print()



            print("\n* Registros de transferências no mês e ano informados:")
            print()
            for conta in result_conta:
                self.__id_conta = conta[0]
                query_transferencia = "SELECT * FROM Transferencia WHERE id_conta_origem = " + \
                    str(self.__id_conta)
                self.__cursor.execute(query_transferencia)

                result_transferencia = self.__cursor.fetchall()

                if(result_transferencia == None):
                    print("Nenhuma transferência de dinheiro foi feita no mês e ano informados.")
                else:
                    for a in result_transferencia:
                        data_dividida_em_partes = a[4].split('/')
                        mes_armazenado = data_dividida_em_partes[1]
                        nova_data_dividida_em_partes = data_dividida_em_partes[2]
                        nova_data_dividida_em_partes = nova_data_dividida_em_partes.split(
                            ' ')
                        ano_armazenado = nova_data_dividida_em_partes[0]
                        if(mes == mes_armazenado and ano == ano_armazenado):
                            for i in range(len(y)):
                                if(i == 0):
                                    pass
                                elif(i == 1):
                                    pass
                                elif(i == 2):
                                    nome_coluna = "ID da conta de orígem"
                                    print("%s: %s" % (nome_coluna, a[1]))
                                    nome_coluna = "ID da conta de destino"
                                    print("%s: %s" % (nome_coluna, a[2]))
                                    nome_coluna = "Montante transferido"
                                    print("%s: %s" % (nome_coluna, a[3]))
                                elif(i == 3):
                                    nome_coluna = "Data da operação"
                                    print("%s: %s" % (nome_coluna, a[4]))
                            print("---------------------------------")
                            print()

    # Recupera todos os dados das contas do usuário
    def data_accounts(self, email, senha):

        self.__email_usuario = email
        self.__senha_usuario = senha

        try:
            self.__cursor.execute("SELECT * FROM Usuario WHERE email = %s AND senha = %s;",
                                  (self.__email_usuario, self.__senha_usuario))

            result = self.__cursor.fetchone()

            self.__id_usuario = result[0]

            self.__cursor.execute(
                "SELECT * FROM Conta WHERE id_usuario = " + str(self.__id_usuario))

            contas = self.__cursor.fetchall()

            for conta in contas:
                for i in range(len(conta)):
                    if(i == 0):
                        nome_coluna = "ID da conta"
                        print("%s: %s" % (nome_coluna, conta[0]))
                        pass
                    if(i == 1):
                        nome_coluna = "Tipo da conta"
                        print("%s: %s" % (nome_coluna, conta[1]))
                    elif(i == 2):
                        nome_coluna = "Numero da conta"
                        print("%s: %s" % (nome_coluna, conta[2]))
                    elif(i == 3):
                        nome_coluna = "Senha da conta"
                        print("%s: %s" % (nome_coluna, conta[3]))
                    elif(i == 4):
                        # nome_coluna = "ID do Usuário"
                        # print("%s: %s" %(nome_coluna, conta[4]))
                        pass
                    elif(i == 5):

                        self.__cursor.execute(
                            "SELECT nome FROM Banco WHERE id = " + str(conta[5]))
                        result_nome_banco = self.__cursor.fetchone()

                        if(result_nome_banco == None):
                            pass
                        else:
                            nome_banco = result_nome_banco[0]
                        nome_coluna = "Banco"
                        print("%s: %s" % (nome_coluna, nome_banco))

                    elif(i == 6):
                        nome_coluna = "Agencia"
                        print("%s: %s" % (nome_coluna, conta[6]))
                    elif(i == 7):
                        self.__montante = "R$ " + str(conta[7])
                        nome_coluna = "Montante"
                        print("%s: %s" % (nome_coluna, self.__montante))
                    elif(i == 8):
                        nome_coluna = "Data de Criação"
                        print("%s: %s" % (nome_coluna, conta[8]))
                print("---------------------------------------")
                print()

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Adiciona uma conta
    def add_account(self, tipo_conta, numero_conta, senha, id_usuario, id_banco, agencia, montante=0.00):

        self.__tipo_conta = tipo_conta
        self.__numero_conta = numero_conta
        self.__senha = senha
        self.__id_usuario = id_usuario
        self.__id_banco = id_banco
        self.__agencia = agencia
        self.__montante = montante

        data_tempo_atual = datetime.datetime.now()
        self.__data_de_cadastro = data_tempo_atual.strftime(
            "%d/%b/%Y (%H:%M:%S)")

        query_add_account = """INSERT INTO Conta (tipo_conta, numero_conta, senha, id_usuario, id_banco, agencia, montante, data_de_cadastro) VALUES ('{0}', '{1}', '{2}', {3}, {4}, '{5}', {6}, '{7}')""".format(
            self.__tipo_conta, self.__numero_conta, self.__senha, self.__id_usuario, self.__id_banco, self.__agencia, self.__montante, self.__data_de_cadastro)

        try:
            self.__cursor.execute(query_add_account)
            self.__conn.commit()
        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()

    def integridade_numero_conta(self, numero_conta):

        self.__numero_conta = numero_conta

        query_verificadora = ("SELECT * FROM Conta WHERE numero_conta = '{x1}'".format(x1 = self.__numero_conta))
        self.__cursor.execute(query_verificadora)        
        result = self.__cursor.fetchone()

        if(result == None):
            return True
        else:
            return False

    # Adiciona um depósito de dinheiro na conta informada
    def deposito(self, id_conta, senha_conta, montante):

        self.__id_conta = id_conta
        self.__senha_conta = senha_conta

        self.__cursor.execute(
            "SELECT montante FROM Conta WHERE id = " + str(self.__id_conta))
        result_montante = self.__cursor.fetchone()

        if(result_montante == None):
            return False
        else:
            montante += result_montante[0]
            self.__montante = montante

        montante_string = "R$ " + str(self.__montante)

        data_tempo_atual = datetime.datetime.now()
        self.__data_da_operacao = data_tempo_atual.strftime(
            "%d/%b/%Y (%H:%M:%S)")

        query_register_operation = """INSERT INTO Deposito (id_conta, montante, data_da_operacao) VALUES ({0}, '{1}', '{2}')""".format(
            self.__id_conta, montante_string, self.__data_da_operacao)

        try:
            self.__cursor.execute("UPDATE Conta SET montante = %s WHERE id = %s AND senha = %s;", (str(
                self.__montante), str(self.__id_conta), self.__senha_conta))

            self.__cursor.execute(query_register_operation)

            self.__conn.commit()

            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Saca dinheiro da conta informada
    def saque(self, id_conta, senha_conta, montante):

        montante_sacado = montante

        self.__id_conta = id_conta
        self.__senha_conta = senha_conta

        self.__cursor.execute(
            "SELECT montante FROM Conta WHERE id = %s and senha = %s;", (str(self.__id_conta), self.__senha_conta))
        result_montante = self.__cursor.fetchone()

        if(result_montante == None):
            return False    
        else:
            if(result_montante[0] == 0):
                print("\nSua conta está zerada, portanto não é possível sacar dinheiro!")
                return False
            elif(result_montante[0] < montante_sacado):
                print("\nSua conta possui menos dinheiro do que a quantidade requisitada, portanto não é possível sacar dinheiro!")
                return False
            else:
                montante -= result_montante[0]
                montante = abs(montante)
                self.__montante = montante

        montante_string = "R$ " + str(montante_sacado)

        data_tempo_atual = datetime.datetime.now()
        self.__data_da_operacao = data_tempo_atual.strftime(
            "%d/%b/%Y (%H:%M:%S)")

        query_register_operation = """INSERT INTO Saque (id_conta, montante, data_da_operacao) VALUES ({0}, '{1}', '{2}')""".format(
            self.__id_conta, montante_string, self.__data_da_operacao)

        try:
            self.__cursor.execute("UPDATE Conta SET montante = %s WHERE id = %s AND senha = %s;", (str(
                self.__montante), str(self.__id_conta), self.__senha_conta))

            self.__cursor.execute(query_register_operation)

            self.__conn.commit()

            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Transfere dinheiro entre duas contas
    def transferencia(self, numero_conta_origem, senha_conta_origem, numero_conta_destino, montante_origem):

        montante_transferido = montante_origem
        montante_destino = montante_transferido

        self.__numero_conta_origem = numero_conta_origem
        self.__senha_conta_origem = senha_conta_origem
        self.__cursor.execute(
            "SELECT * FROM Conta WHERE numero_conta = %s AND senha = %s", (self.__numero_conta_origem, self.__senha_conta_origem))
        result_conta_origem = self.__cursor.fetchone()
        if(result_conta_origem == None):
            print("\nOs dados informados da conta orígem estão incorretos ou não existem.")
            return False
        else:
            self.__id_conta_origem = result_conta_origem[0]
            self.__cursor.execute(
            "SELECT montante FROM Conta WHERE id = " + str(self.__id_conta_origem))
            result_montante_origem = self.__cursor.fetchone()

        self.__numero_conta_destino = numero_conta_destino
        query_conta_destino = ("SELECT * FROM Conta WHERE numero_conta = '{x1}'".format(x1 = self.__numero_conta_destino))
        self.__cursor.execute(query_conta_destino)
        result_conta_destino = self.__cursor.fetchone()
        if(result_conta_destino == None):
            print("\nOs dados informados da conta destino estão incorretos ou não existem.")
            return False
        else:
            self.__id_conta_destino = result_conta_destino[0]

        self.__cursor.execute(
            "SELECT montante FROM Conta WHERE id = " + str(self.__id_conta_origem))
        result_montante_origem = self.__cursor.fetchone()

        if(result_montante_origem == None):
            return False
        else:
            if(result_montante_origem[0] == 0):
                print("\nSua conta está zerada, portanto não é possível transferir dinheiro!")
                return False
            elif(result_montante_origem[0] < montante_transferido):
                print("\nSua conta possui menos dinheiro do que a quantidade solicitada, portanto não é possível transferir dinheiro!")
                return False
            else:
                montante_origem -= result_montante_origem[0]
                montante_origem = abs(montante_origem)
                self.__montante_origem = montante_origem

        montante_string = "R$ " + str(montante_transferido)

        data_tempo_atual = datetime.datetime.now()
        self.__data_da_operacao = data_tempo_atual.strftime(
            "%d/%b/%Y (%H:%M:%S)")

        query_register_operation = """INSERT INTO Transferencia (id_conta_origem, id_conta_destino, montante, data_da_operacao) VALUES ({0}, {1}, '{2}', '{3}')""".format(
            self.__id_conta_origem, self.__id_conta_destino, montante_string, self.__data_da_operacao)

        self.__cursor.execute(
            "SELECT montante FROM Conta WHERE id = " + str(self.__id_conta_destino))
        result_montante_destino = self.__cursor.fetchone()

        if(result_montante_destino == None):
            return False
        else:
            montante_destino += result_montante_destino[0]
            self.__montante_destino = montante_destino

        try:
            self.__cursor.execute("UPDATE Conta SET montante = %s WHERE id = %s AND senha = %s;", (str(
                self.__montante_origem), str(self.__id_conta_origem), self.__senha_conta_origem))

            self.__cursor.execute("UPDATE Conta SET montante = %s WHERE id = %s;", (str(
                self.__montante_destino), str(self.__id_conta_destino)))

            self.__cursor.execute(query_register_operation)

            self.__conn.commit()

            return True

        except mysql.connector.Error as err:
            print(err)
            self.__conn.rollback()
            return False

    # Aborta a conexão com o BD
    def connection_close(self):
        self.__conn.close()

##################################################################################################################

