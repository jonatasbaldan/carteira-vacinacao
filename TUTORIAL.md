# Iniciando o projeto

## 1. Instale o Python

Link: https://www.python.org/downloads/
Obs: Não se esqueça de marcar a opção de adicionar o python no PATH

## 2. Instale o Django

Abra o terminal do seu Sistema operacional e digite o código:

```Linux
python -m pip install Django
```

```Windows
python -m pip install Django
```

## 3. Instale o driver do Mysql para Python

Abra o terminal e digite o códgio:

```
pip install mysqlclient
```

OBS: Caso der um aviso que tem uma versão recente, instale a recente.

## 4. Instale o MySQL e crie uma tabela

Link para o download no Windows: https://dev.mysql.com/downloads/installer/

(Quando chegar na aba de selecionar os produtos, por via das dúvidas, selecione todos)

e depois, crie uma tabela chamada `petshop`.

## 5. Clone o projeto

### 1. Baixe o Git

Site para o Download: https://git-scm.com/

e instale normalmente.

### 2. Clone o projeto

Crie uma pasta aonde o projeto vá ficar e, depois, no terminal do seu Sistema Operacional, digite:

```cmd
git clone https://github.com/jonatasbaldan/carteira-vacinacao.git
```

Ou baixe o arquivo .zip e extraia aonde preferir.

## 6. Configurando o projeto

Abra o projeto na sua IDE de preferência (que pelo menos tenha suporte para python).

Depois, abra o seu terminal na pasta do seu projeto e digite:
```cmd
python manage.py migrate
```

Esse comando acima é para sincroniar/criar do django no banco de dados.

## 7. iniciando o Projeto

Na pasta do projeto, digite no seu terminal:

```cmd
python manage.py runserver
```

E depois, para abrir o projeto no navegador, digite nele:

```http
http://127.0.0.1:8000/website/
```
