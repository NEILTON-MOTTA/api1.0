raise Exception("TESTE EASY PANEL")
from fastapi import FastAPI
from routes import cliente              # importa cliente.py
from routes import valida_usuario       # importa valida_usuario.py
from routes import numerador_clientes   # importa valida_usuario.py
from routes import produto              # importa produto.py

#app = FastAPI()
app = FastAPI(
    title="API DYNACONTROL"
)

@app.get("/teste-versao ZZ")
def teste_versao():
    return {"versao": "BUILD TESTE"}


app.include_router(cliente.router)
app.include_router(valida_usuario.router)
app.include_router(numerador_clientes.router)
app.include_router(produto.router)

