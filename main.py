from fastapi import FastAPI 
app = FastAPI()
@app.get("/mensagem-ok")
async def mensagem_inicial():
    return{"mensagem:" "ok"}