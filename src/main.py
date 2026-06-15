from fastapi import FastAPI
app = FastAPI(title='IDP Agent')


@app.get('/health')
def health():
    return {'status':'ok'}
