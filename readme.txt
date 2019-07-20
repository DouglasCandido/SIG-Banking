- O sistema precisa de duas bibliotecas que podem ser instaladas facilmente utilizando o pip.

* Para começar a usar, precisa criar o banco de dados através do arquivo bd_sig_banking.sql
- Cadastrar alguns bancos (Instituições) no sistema. Isso pode ser feito rodando o script testes.py
- Feito isso, poderá prosseguir com o cadastro de usuário e experimentar o sistema.

pip install getpass
pip install validate_email

* Desenvolvido: 

> Validação do número da conta bancária:

Expressão regular: ^[1-9]{9}\-[1-9]{1}$

A explicação completa dela é:

^ - Início da String
[1-9]{9} - 9 dígitos, na faixa de 1 à 9
\- - Hífen
[1-9]{1} - 1 dígito verificador, na faixa de 1 à 9

> Validação do número da agência:

Expressão regular: ^[1-9]{4}$

A explicação completa dela é:
^ - Início da String
[1-9]{4} - 4 dígitos, na faixa de 1 à 9

> Validação de CPF:

Expressão regular: ^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$

A explicação completa dela é:

^ - Início da String
[0-9]{3} - 3 dígitos, na faixa de 0 à 9
\. - Ponto
[0-9]{3} - 3 dígitos, na faixa de 0 à 9
\. - Ponto
[0-9]{3} - 3 dígitos, na faixa de 0 à 9
\- - Hífen
[0-9]{2} - 2 dígitos verificadores, na faixa de 0 à 9

> Validação de CNPJ:

Expressão regular: ^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$

A explicação completa dela é:

^ - Início da String
[0-9]{3} - 2 dígitos, na faixa de 0 à 9
\. - Ponto
[0-9]{3} - 3 dígitos, na faixa de 0 à 9
\. - Ponto
[0-9]{3} - 3 dígitos, na faixa de 0 à 9
\/ - Barra
[0-9]{3} - 4 dígitos, na faixa de 0 à 9
\- - Hífen
[0-9]{2} - 2 dígitos verificadores, na faixa de 0 à 9

> Validação do número da agência:

Expressão regular: ^[1-9]{4}$

A explicação completa dela é:
^ - Início da String
[1-9]{4} - 4 dígitos, na faixa de 1 à 9

* Retirado do site Stack Overflow:

> Validação de telefones:

Expressão Regular: ^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$

A explicação completa dela é:

Hoje em dia todos os telefones celulares no Brasil têm nove dígitos e iniciam com o dígito 9 e todos os telefones fixos têm 8 dígitos e nunca iniciam com o dígito 9. Eu pessoalmente preferiria formatar o telefone como (xx) xxxxx-xxxx. Assim sendo, a melhor expressão regular para isso seria essa:

^ - Início da string.
\( - Um abre parênteses.
[1-9]{2} - Dois dígitos de 1 a 9. Não existem códigos de DDD com o dígito 0.
\) - Um fecha parênteses.
  - Um espaço em branco.
(?:[2-8]|9[1-9]) - O início do número. Representa uma escolha entre o um dígito entre 2 e 8 (a parte do [2-8]) e de um 9 seguido de um dígito de 1 a 9 (a parte do 9[1-9]). O | separa as opções a serem escolhidas. O (?: ... ) agrupa tais escolhas. Telefones fixos começam com dígitos de 2 a 8. Telefones celulares começam com 9 e têm um segundo dígito de 1 a 9. O primeiro dígito nunca será 0 ou 1. Celulares não podem começar com 90 porque esse é o prefixo para ligações a cobrar.
[0-9]{3} - Os demais três dígitos da primeira metade do número do telefone, perfazendo um total de 4 ou 5 dígitos na primeira metade.
\- - Um hífen.
[0-9]{4} - A segunda metade do número do telefone.
$ - Final da string.


