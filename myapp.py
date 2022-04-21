"""Pruebas de FastAPI"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def say_hi():
    """Funcion de retorno comentario"""
    return 'Hola soy Juandi'

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
