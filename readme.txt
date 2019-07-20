- O sistema precisa de duas bibliotecas que podem ser instaladas facilmente utilizando o pip.

* Para come�ar a usar, precisa criar o banco de dados atrav�s do arquivo bd_sig_banking.sql
- Cadastrar alguns bancos (Institui��es) no sistema. Isso pode ser feito rodando o script testes.py
- Feito isso, poder� prosseguir com o cadastro de usu�rio e experimentar o sistema.

pip install getpass
pip install validate_email

* Desenvolvido: 

> Valida��o do n�mero da conta banc�ria:

Express�o regular: ^[1-9]{9}\-[1-9]{1}$

A explica��o completa dela �:

^ - In�cio da String
[1-9]{9} - 9 d�gitos, na faixa de 1 � 9
\- - H�fen
[1-9]{1} - 1 d�gito verificador, na faixa de 1 � 9

> Valida��o do n�mero da ag�ncia:

Express�o regular: ^[1-9]{4}$

A explica��o completa dela �:
^ - In�cio da String
[1-9]{4} - 4 d�gitos, na faixa de 1 � 9

> Valida��o de CPF:

Express�o regular: ^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$

A explica��o completa dela �:

^ - In�cio da String
[0-9]{3} - 3 d�gitos, na faixa de 0 � 9
\. - Ponto
[0-9]{3} - 3 d�gitos, na faixa de 0 � 9
\. - Ponto
[0-9]{3} - 3 d�gitos, na faixa de 0 � 9
\- - H�fen
[0-9]{2} - 2 d�gitos verificadores, na faixa de 0 � 9

> Valida��o de CNPJ:

Express�o regular: ^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$

A explica��o completa dela �:

^ - In�cio da String
[0-9]{3} - 2 d�gitos, na faixa de 0 � 9
\. - Ponto
[0-9]{3} - 3 d�gitos, na faixa de 0 � 9
\. - Ponto
[0-9]{3} - 3 d�gitos, na faixa de 0 � 9
\/ - Barra
[0-9]{3} - 4 d�gitos, na faixa de 0 � 9
\- - H�fen
[0-9]{2} - 2 d�gitos verificadores, na faixa de 0 � 9

> Valida��o do n�mero da ag�ncia:

Express�o regular: ^[1-9]{4}$

A explica��o completa dela �:
^ - In�cio da String
[1-9]{4} - 4 d�gitos, na faixa de 1 � 9

* Retirado do site Stack Overflow:

> Valida��o de telefones:

Express�o Regular: ^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$

A explica��o completa dela �:

Hoje em dia todos os telefones celulares no Brasil t�m nove d�gitos e iniciam com o d�gito 9 e todos os telefones fixos t�m 8 d�gitos e nunca iniciam com o d�gito 9. Eu pessoalmente preferiria formatar o telefone como (xx) xxxxx-xxxx. Assim sendo, a melhor express�o regular para isso seria essa:

^ - In�cio da string.
\( - Um abre par�nteses.
[1-9]{2} - Dois d�gitos de 1 a 9. N�o existem c�digos de DDD com o d�gito 0.
\) - Um fecha par�nteses.
  - Um espa�o em branco.
(?:[2-8]|9[1-9]) - O in�cio do n�mero. Representa uma escolha entre o um d�gito entre 2 e 8 (a parte do [2-8]) e de um 9 seguido de um d�gito de 1 a 9 (a parte do 9[1-9]). O | separa as op��es a serem escolhidas. O (?: ... ) agrupa tais escolhas. Telefones fixos come�am com d�gitos de 2 a 8. Telefones celulares come�am com 9 e t�m um segundo d�gito de 1 a 9. O primeiro d�gito nunca ser� 0 ou 1. Celulares n�o podem come�ar com 90 porque esse � o prefixo para liga��es a cobrar.
[0-9]{3} - Os demais tr�s d�gitos da primeira metade do n�mero do telefone, perfazendo um total de 4 ou 5 d�gitos na primeira metade.
\- - Um h�fen.
[0-9]{4} - A segunda metade do n�mero do telefone.
$ - Final da string.


