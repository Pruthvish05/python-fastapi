from fastapi import FastAPI
import uvicorn
app = FastAPI()
text_posts = {
    1: {"id": 1, "content": "Hello, this is my first post!"},
    2: {"id": 2, "content": "FastAPI is great for building APIs!"}
}
@app.get("/posts")
def read_posts():
    return text_posts


@app.get("/posts/{post_id}")
def read_post(post_id: int):
    return text_posts.get(post_id, {"error": "Post not found"})
