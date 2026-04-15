from sqlalchemy.orm import Session
import models,schemas
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
#this file contains all the curd operations
#as the name suggests
def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    try:
        db.commit()
        db.refresh(db_note)
    except:
        db.rollback()
        raise
    return db_note

def get_notes(db: Session):
    return db.query(models.Note).all()

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def update_note(db: Session, note_id: int, note: schemas.NoteCreate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        return None
    db_note.title = note.title
    db_note.content = note.content
    try:
        db.commit()
        db.refresh(db_note)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return db_note

def delete_note(db: Session, note_id: int):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        return None
    db.delete(note)
    try:
        db.commit()
    except:
        db.rollback()
        raise
    return note

def get_paginationed_notes(db: Session, page: int, limit: int):
    offset = (page - 1) * limit
    total = db.query(models.Note).count()
    notes = db.query(models.Note).offset(offset).limit(limit).all()
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "has_next": offset + limit < total,
        "has_prev": offset > 0,
        "notes": notes,
    }
