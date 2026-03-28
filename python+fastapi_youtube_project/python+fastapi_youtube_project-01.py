from fastapi import FastAPI
app = FastAPI()
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
]
@app.get("/books")
def read_books():
    return {"books": books}
@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"book": book}
    return {"error": "Book not found"}
@app.post("/books")
def create_book(book: dict):
    book_id = len(books) + 1
    new_book = {"id": book_id, "title": book["title"], "author": book["author"]}
    books.append(new_book)
    return {"book": new_book}
@app.put("/books/{book_id}")
def update_book(book_id: int, book: dict):
    for b in books:
        if b["id"] == book_id:
            b["title"] = book["title"]
            b["author"] = book["author"]
            return {"book": b}
    return {"error": "Book not found"}
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}