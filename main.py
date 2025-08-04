from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, Game
from database import engine, SessionLocal
from pydantic import BaseModel

app = FastAPI(root_path="/games")

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class GameCreate(BaseModel):
    name: str

@app.get("/")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    return games

@app.post("/")
def add_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = Game(name=game.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game