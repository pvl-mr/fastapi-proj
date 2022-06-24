from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# get - operation
# /- pathlib
# def index() - path operation function
# @app.get('/')  - path operation decorator

#'/blog&limit=10&published=true'
#limit - query parameter can be received or not
@app.get('/blog')
def index(published: bool = True, limit=10, sort: Optional[str] = None):
    if published:
        return {
            'data': f'{limit} published blogs from db'
        }
    else:
        return {
            'data': f'{limit} all blogs from db'
        }


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

#id - path parameter
@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return limit
    # return {'data': {'2', '1'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is  with title as {request.title}'}