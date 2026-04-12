from pydantic import BaseModel
#this file contains all the schemas for the notes
#schemas are to define the structure of the data 
#they are like a wall between the database and the user
#they are used to validate the data and to serialize the data
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

class UserCreate(BaseModel):
    email: str
    password: str

class userlogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str