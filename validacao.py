import re
import validate_email

def validaEmail(email):

	email = email

	is_valid = validate_email.validate_email(email)

	if(is_valid == True):
		return True
	else:
		return False

def validaTelefone(telefone):

	telefone = telefone

	regex = '^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$';

	match = re.search(regex, telefone)
	
	if((match is None) == True):
		return False
	else:
		return True

def validaCPF(cpf):

	cpf = cpf

	regex = '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'; # Essa foi eu que fiz

	match = re.search(regex, cpf)
	
	if((match is None) == True):
		return False
	else:
		return True

def validaCNPJ(cnpj):

	cnpj = cnpj

	regex = '^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$'; # Essa foi eu que fiz

	match = re.search(regex, cnpj)
	
	if((match is None) == True):
		return False
	else:
		return True

def validaNumeroConta(numero_conta):

	numero_conta = numero_conta

	tamanho = len(numero_conta)

	regex = '^[1-9]{9}\-[1-9]{1}$' # Essa foi eu que fiz 

	match = re.search(regex, numero_conta)

	if(tamanho > 20):
		return False
	elif((match is None) == True):
		return False
	else:
		return True

def validaAgencia(agencia):

	agencia = agencia

	tamanho = len(agencia)

	regex = '^[1-9]{4}$' # Essa foi eu que fiz 

	match = re.search(regex, agencia)

	if(tamanho != 4):
		return False
	elif((match is None) == True):
		return False
	else:
		return True
