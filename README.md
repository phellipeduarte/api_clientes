# API REST - CRUD completo de Clientes

API REST que acessa um banco PostgreSQL e cria, lista, atualiza e deleta clientes utilizando o Flask e algumas ferramentas como:

- flask_sqlalchemy
- flask_restplus
- flask_marshmallow
- marshmallow_sqlalchemy
- psycopg2

---

## Como rodar o projeto?

1. Instale o [python](https://www.python.org/downloads/)

2. Instale as dependências do arquivo requirements.txt, no terminal digite:

```
pip install -r requirements.txt
```
3. Com o [git](https://git-scm.com/downloads) instalado, clone esse repositório:
```
git clone https://github.com/phellipeduarte/api_clientes
```
4. Com o terminal aberto no endereço da pasta do repositório baixado, digite:
```
python app.py
```
5. Por fim, acesse a [URL](http://localhost:5000/api/doc) com a documentação da API, onde é possível fazer as requisições

#

- **Lembrete**: Essa API foi feita utilizando uma instância local do PostgreSQL, logo, é necessário instanciar um banco Postgre e alterar a variável "db_URI" no arquivo db.py, localizado na raiz do projeto
