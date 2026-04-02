from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()
Notes = []
class Note(BaseModel):
    title: str
    content: str
#Root endpoint i really dont know but yea.
@app.get("/")
def root():
    return {"message": "Welcome to the Smart Notes Tracker"}


@app.post("/notes")
def create_note(note: Note):
    note_dict = note.dict()
    note_dict["id"] = len(Notes) + 1
    Notes.append(note_dict)
    return {"message": "Note created successfully", "note": note}

@app.get("/notes")
def get_notes():
    return {"notes": Notes}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in Notes:
        if note["id"] == note_id:
            return {"note": note}
    raise HTTPException(status_code=404, detail="Note not found")          

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in Notes:
        if note["id"] == note_id:
            Notes.remove(note)
            len(Notes) - 1
            return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")
