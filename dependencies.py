from core.database import SessionLocal

def abrir_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
         