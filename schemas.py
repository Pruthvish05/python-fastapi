from pydantic import BaseModel

class TextPost(BaseModel):
    id: int
    content: str