from fastapi import FastAPI, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
import sqlite3

con=sqlite3.connect('game.db', check_same_thread=False)
cur=con.cursor()

app = FastAPI()
SECRET="super-coding"
manager=LoginManager(SECRET, '/login')

@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS=f'id="{data}"'
    
    if type(data)==dict:
        WHERE_STATEMENTS=f'''id="{data['id']}"'''
        
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    user=cur.execute(f"""
                     SELECT * FROM members WHERE {WHERE_STATEMENTS}
                     """).fetchone()
    return user

@app.post('/games')
def create_game(title:Annotated[str, Form()],description:Annotated[str, Form()], word1:Annotated[str, Form()],word2:Annotated[str, Form()],word3:Annotated[str, Form()],word4:Annotated[str, Form()],word5:Annotated[str, Form()],word6:Annotated[str, Form()],word7:Annotated[str, Form()],word8:Annotated[str, Form()],word9:Annotated[str, Form()],word10:Annotated[str, Form()]):
    cur.execute(f"""
                INSERT INTO 
                games (title, description, word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)
                VALUES ('{title}', '{description}', '{word1}', '{word2}', '{word3}', '{word4}', '{word5}', '{word6}', '{word7}', '{word8}','{word9}','{word10}');
                """)
    con.commit()
    return '200'
    
    
@app.post('/signup')
def signup(id:Annotated[str, Form()], password:Annotated[str, Form()], name:Annotated[str, Form()],email:Annotated[str, Form()]):
    cur.execute(f"""
                INSERT INTO members (id, password, name, email)
                VALUES ('{id}', '{password}','{name}','{email}')
                """)
    con.commit()
    return '200'

@app.post('/login')
def login(id:Annotated[str, Form()], password:Annotated[str, Form()]):
    user=query_user(id)
    
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    
    return '200'
    
    
    
app.mount("/", StaticFiles(directory="static", html=True), name="static")

