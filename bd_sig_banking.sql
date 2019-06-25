create schema bd_sig_banking;
use bd_sig_banking;

create table if not exists Uf(
    id int not null auto_increment unique,
    sigla varchar(2) not null unique,
    nome varchar(25) not null unique,
    primary key(id) 
); 

insert into uf(sigla, nome) values("AC","Acre");
insert into uf(sigla, nome) values("AL","Alagoas");
insert into uf(sigla, nome) values("AP","Amapá");
insert into uf(sigla, nome) values("AM","Amazonas");
insert into uf(sigla, nome) values("BA","Bahia");
insert into uf(sigla, nome) values("CE","Ceará");
insert into uf(sigla, nome) values("DF","Distrito Federal");
insert into uf(sigla, nome) values("ES","Espírito Santo");
insert into uf(sigla, nome) values("GO","Goiás");
insert into uf(sigla, nome) values("MA","Maranhão");
insert into uf(sigla, nome) values("MT","Mato Grosso");
insert into uf(sigla, nome) values("MS","Mato Grosso do Sul");
insert into uf(sigla, nome) values("MG","Minas Gerais");
insert into uf(sigla, nome) values("PA","Pará");
insert into uf(sigla, nome) values("PB","Paraíba");
insert into uf(sigla, nome) values("PR","Paraná");
insert into uf(sigla, nome) values("PE","Pernambuco");
insert into uf(sigla, nome) values("PI","Piauí");
insert into uf(sigla, nome) values("RJ","Rio de Janeiro");
insert into uf(sigla, nome) values("RN","Rio Grande do Norte");
insert into uf(sigla, nome) values("RS","Rio Grande do Sul");
insert into uf(sigla, nome) values("RO","Rondônia");
insert into uf(sigla, nome) values("RR","Roraima");
insert into uf(sigla, nome) values("SC","Santa Catarina");
insert into uf(sigla, nome) values("SP","São Paulo");
insert into uf(sigla, nome) values("SE","Sergipe");
insert into uf(sigla, nome) values("TO","Tocantins");

CREATE TABLE `Banco` (
  `id` int(11) NOT NULL auto_increment unique,
  `cnpj` varchar(18) NOT NULL unique,
  `nome` varchar(50) NOT NULL unique,
  `email` varchar(50) NOT NULL unique,
  # `telefone` varchar(12) NOT NULL,
  primary key(id)
);

CREATE TABLE `Usuario` (
  `id` int(11) NOT NULL auto_increment unique,
  `tipo_pessoa` varchar(1) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `sobrenome` varchar(50) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `email` varchar(50) NOT NULL unique,
  `senha` varchar(16) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `id_uf` int(11) NOT NULL,
  `cidade` varchar(30) NOT NULL,
  `bairro` varchar(30) NOT NULL,
  `rua` varchar(30) NOT NULL,
  `numero_casa` varchar(30) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `cnpj` varchar(18) DEFAULT NULL,
  `data_de_cadastro` varchar(30) NOT NULL,
  primary key (id),
  foreign key(id_uf) references Uf(id)
);

CREATE TABLE `Conta` (
  `id` int(11) NOT NULL auto_increment unique,
  `tipo_conta` varchar(3) NOT NULL,
  `numero_conta` varchar(11) NOT NULL unique,
  `senha` varchar(16) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_banco` int(11) NOT NULL,
  `agencia` varchar(4) NOT NULL,
  `montante` float8 DEFAULT 0.00,
  `data_de_cadastro` varchar(30) NOT NULL, 
  primary key (id),
  foreign key(id_usuario) references Usuario(id),
  foreign key(id_banco) references Banco(id)
);

CREATE TABLE `Deposito` ( 
  `id` int(11) NOT NULL auto_increment unique,
  `id_conta` int(11) NOT NULL,
  `montante` varchar(100) NOT NULL,
  `data_da_operacao` varchar(30) NOT NULL,
  primary key (id),
  foreign key(id_conta) references Conta(id)
);

CREATE TABLE `Saldo` ( 
  `id` int(11) NOT NULL auto_increment unique, 
  `id_conta` int(11) NOT NULL,
  `montante_na_data_da_operacao` varchar(100) NOT NULL,
  `data_da_operacao` varchar(30) NOT NULL,
  primary key (id),
  foreign key(id_conta) references Conta(id)
);




