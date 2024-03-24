
# Teste IviJur

Repositório destinado ao teste prático realizado para estagiário na empresa IviJur 

REQUISITOS

Os seguintes pacotes são obrigatórios para rodar os códigos:
- Requests
- Uvicorn
- FastAPI

ATIVIDADES
#### 1- Escreva uma função em Python que receba uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original, multiplicados por 2.

```python
lista = [1, 2, 3, 4]
def pares(lista: list):
    lista2 = []
    for number in lista:
        if number % 2 == 0:
            lista2.append(number*2)
    return lista2
print(pares(lista))
```
Foi criada uma lista para armazenar os novos numeros obtidos após a operação. Não foi especificado mas, se necessário realizar o input dos dados do usuário, seria utilizada a função "input()" para tal.
```python
lista = list(input("insira a lista de números separados por vírgula"))
```

#### 2- Crie um pequeno aplicativo FastAPI que tenha um endpoint POST /create-user, que aceite um "username" e "email" no corpo da solicitação, e um endpoint GET /get-user/{user_id} que retorne os dados de um usuário baseado em um ID fornecido.

Primeiro iniciallizamos o servidor com o Uvicorn.

```python
from fastapi import FastAPI, Path
from pydantic import BaseModel
import requests 

app = FastAPI() 
```
```
uvicorn <nome programa>:app --reload
```
Com isso, todas as APIs foram utilizadas e testadas utilizando o "/docs" na URL local. Essa prática foi feita em consonância com o descrito na documentação do FastAPI.

```python
@app.post("/create-user/{user-id}")
def create_user(user_id: int, user: User):
    if user_id in users:
        return {"Error": "User exist"}
    users[user_id] = user 
    return users[user_id]

@app.get("/get-user/{user_id}")
def get_user(user_id: int):
    return users[user_id] 
```

#### 3- Utilizando Python, faça uma requisição à API pública JSONPlaceholder (https://jsonplaceholder.typicode.com/) para obter posts de usuários. Depois, exponha esses dados através de um endpoint FastAPI. Descreva como você faria a autenticação se a API exigisse um token de acesso.

Utilizando o mesmo servidor, foram feitas as APIs solicitadas na questão. Desta vez foi necessário acessar uma API externa para obter os dados necessários. 

```python
@app.get("/get-posts/")
def get_posts():
    posts = pegaDados("https://jsonplaceholder.typicode.com/posts")
    return posts

@app.get("/get-n-posts/{n_posts}")
def get_n_posts(n_posts: int):
    initialsPosts = []
    posts = pegaDados("https://jsonplaceholder.typicode.com/posts")
    for post in posts[0:n_posts]:
        initialsPosts.append(post)
    return initialsPosts

@app.get("/get-post-by-id/{post_id}")
def get_post_by_id(post_id: int = Path(lt=101)):
    posts = pegaDados("https://jsonplaceholder.typicode.com/posts")
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"Error": "This post does not exist"}

def pegaDados(url: str):
    r = requests.get(url) 
    return r.json()
```
Caso houvesse a necessidade de autenticação por token:
1- Inicialmente é necessário ter o token separado para permitir o acesso ao documento.
2- Após, precisaríamos passar o token como autenticação no requeests para que a api valide.
3- Após, seria necessário que a api validasse a autenticação e permitisse o acesso às informações.

Tal descrição segue o disposto na documentação https://requests.kennethreitz.org/en/latest/user/quickstart/#custom-headers

#### 4-Você recebeu um arquivo JSON contendo dados de vendas de produtos (produto, quantidade, preço). Escreva um script Python que calcule o total de vendas (quantidade * preço) para cada produto e retorne o nome do produto mais vendido.

Foi criado um arquivo sintético para simular o arquivo json descrito na questão, representando uma lista de vendas com sete produtos diferentes. Para facilitar a criação e manipulação do arquivo, o nome do produto foi convertido para um "ID".
```json
{"productID":2,"price":12,"quantity":2}
```
