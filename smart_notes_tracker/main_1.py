from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from requests import Session
#we add somethings ukwim.
from database import SessionLocal, engine, Base
import models
Base.metadata.create_all(bind=engine)
app = FastAPI()
# Notes = []#done with this temporary storagefor notes
class NoteCreate(BaseModel):
    title: str
    content: str

#now we connect to the database and create tables
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Root endpoint i really dont know but yea.
@app.get("/")
def root():
    return {"message": "Welcome to the Smart Notes Tracker"}


@app.post("/notes")
def create_note(note: NoteCreate, db:Session = Depends(get_db)):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {"message": "Note created successfully", "note": db_note}


@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return {"notes": db.query(models.Note).all()}

@app.get("/notes/{note_id}")
def get_note(note_id: int,db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"note": note}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
