from pydantic import BaseModel

class noteBase(BaseModel):
    title: str
    content: str

class NoteCreate(noteBase):
    pass

class NoteResponse(noteBase):
    id: int

    class Config:
        orm_mode = True

class PaginationedNotes(BaseModel):
    total: int
    page: int
    limit: int
    notes: list[NoteResponse]