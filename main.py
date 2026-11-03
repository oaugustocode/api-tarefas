from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def mensagem_inicial():
    return{"status": "ok"}