from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

@router.get("/notes", response_model=list[schemas.NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@router.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    updated_note = crud.update_note(db, note_id, note)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/notes/{note_id}", response_model=schemas.NoteResponse)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = crud.delete_note(db, note_id)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return deleted_note