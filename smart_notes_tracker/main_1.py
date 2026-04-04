from webbrowser import get

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from sqlalchemy.orm import Session
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
#just a start for the site
@app.get("/")
def root():
    return {"message": "Welcome to the Smart Notes Tracker"}

#creating a note endpoint
@app.post("/notes")
def create_note(note: NoteCreate, db:Session = Depends(get_db)):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {"message": "Note created successfully", "note": db_note}

#getting all notes from the database
@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return {"notes": db.query(models.Note).all()}
#getting a single note by id
@app.get("/notes/{note_id}")
def get_note(note_id: int,db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"note": note}


#creating a note update endpoint
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return {"message": "Note updated successfully", "note": db_note}

#creating a note delete endpoint
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
