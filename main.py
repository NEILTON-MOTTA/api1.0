from fastapi import FastAPI
from routes import cliente              # importa cliente.py
from routes import valida_usuario       # importa valida_usuario.py
from routes import numerador_clientes   # importa valida_usuario.py
from routes import produto              # importa produto.py

#app = FastAPI()
app = FastAPI(
    title="API  X"
)

@app.get("/teste-versao 2026.06.03-002")
def teste_versao():
    return {"versao": "2026.06.03-002"}


app.include_router(cliente.router)
app.include_router(valida_usuario.router)
app.include_router(numerador_clientes.router)
app.include_router(produto.router)

