from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {
            'name': 'mariya'
        }
    }

@app.get('/about')
def about():
    return {'data': 'aboutpage'}