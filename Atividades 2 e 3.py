###ATIVIDADE 2

from fastapi import FastAPI, Path
from pydantic import BaseModel
import requests 

app = FastAPI() 

class User(BaseModel):
    username: str
    email: str

users = {}

@app.get("/")
def index():
    return {'username': 'email'}

@app.post("/create-user/{user-id}")
def create_user(user_id: int, user: User):
    if user_id in users:
        return {"Error": "User exist"}
    users[user_id] = user 
    return users[user_id]

@app.get("/get-user/{user_id}")
def get_user(user_id: int):
    return users[user_id] 

## ATIVIDADE 3

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

## 1- Inicialmente é necessário ter o token separado para permitir o acesso ao documento
## 2- Após, precisamos passar o token como autenticação no requeests para que a api valide
## 3- Após é necessário que a api validar a autenticação e permita o acesso às informações



