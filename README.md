# Projeto de TCC
## Passos para reprodução do sistema
 **OBS:** Os comandos utilizados são baseados no sistema operecional o qual o projeto foi desenvolvido:
 - Ubuntu 22.04.5 LTS
 - Ubuntu 24.04.4 LTS

## 1. Instalação de dependencias do sistema:
sudo apt update && sudo apt upgrade -y
sudo apt install -y \ 
git \ 
python3 \ 
python3-pip \ 
python3-venv \ 
python3-full \ 
python3-dev \ 
postgresql \ 
postgresql-contrib \ 
libpq-dev 

## 2. Criação do ambiente virtual:
python3 -m venv env

## 3. Ativar ambiente virtual: 
source env/bin/activate

## 4. Instalação de bibliotecas do arquivo requeriments.py:
pip install -r requirements.txt

## 5. Configurar o PostgreSQL:
### 5.1. Entrar no usuário postgres:
sudo -u postgres psql
### 5.2. Criar o banco de dados:
CREATE DATABASE bancotcc;
### 5.3. Criar usuário e senha:
CREATE USER django WITH PASSWORD 'teste1';
### 5.4. Alterar codificação do usuário:
ALTER ROLE django SET client_encoding TO 'utf8';
### 5.5. Alterar nível de isolamento de transações:
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
### 5.6. Usar fuso horário de São Paulo:
ALTER ROLE django SET timezone TO 'America/Sao_Paulo';
### 5.7. Garantir acesso ao banco:
GRANT ALL PRIVILEGES ON DATABASE myproject TO myproject_user;
### 5.8. Sair do posgre:
\q

**OBS:** Os nomes do banco de dados, do usuário e da senha apresentados acima correspondem à configuração original do projeto. Caso sejam alterados, as mesmas alterações deverão ser realizadas no arquivo *settings.py*, localizado na pasta *projetoSD*.

## 6. Fazer as micrações e executar o projeto:
./manage.py migrate
./manage.py runserver
