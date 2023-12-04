# API REST - CRUD completo de Clientes

API REST que acessa um banco PostgreSQL e cria, lista, atualiza e deleta clientes utilizando o Flask e algumas ferramentas como:

- flask_sqlalchemy
- flask_restplus
- flask_marshmallow
- marshmallow_sqlalchemy
- psycopg2

---

## Imagens:

![Imagem de exemplo da documentação](https://user-images.githubusercontent.com/67296380/133320029-8f7d10bb-db6c-445a-9f98-3e90bcc99464.png)
<div align="center">
  
*Documentação da API com o Swagger*
  
</div>

---

## Como rodar o projeto?

1. Instale o [python](https://www.python.org/downloads/)

2. Crie um ambiente virtual
```
python -m venv nome_do_ambiente

venv\Scripts\activate
```

3. Ative o ambiente virtual
```
nome_do_ambiente\Scripts\activate
```

4. Com o [git](https://git-scm.com/downloads) instalado, clone esse repositório:

```
git clone https://github.com/phellipeduarte/api_clientes
```

5. Instale as dependências do arquivo requirements.txt, no terminal digite:

```
pip install -r requirements.txt
```

6. Com o terminal aberto no endereço da pasta do repositório baixado, digite:
```
python app.py
```
7. Por fim, acesse a [URL](http://localhost:5000/api/doc) com a documentação da API, onde é possível fazer as requisições

#

- **Lembrete**: Essa API foi feita utilizando uma instância local do PostgreSQL, logo, é necessário instanciar um banco Postgre e alterar a variável "db_URI" no arquivo db.py, localizado na raiz do projeto
