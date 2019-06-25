import connection
import validacao
import getpass

running = connection.connection('root', 'douglas', 'localhost', 'bd_sig_banking')

# Cadastro de alguns bancos no sistema:

'''
running.add_bank('00.360.305/0001-04', 'Caixa Econômica Federal', 'cef@cef.com.br')
running.add_bank('00.000.000/0001-91', 'Banco do Brasil S/A', 'bb@bb.com.br')
running.add_bank('60.872.504/0001-23', 'Itaú Unibanco Holding S/A', 'itau@itau.com.br')
running.add_bank('60.746.948.0001-12', 'Banco Bradesco S/A', 'bradesco@bradesco.com.br')
'''

running.connection_close()