from fastapi import FastAPI
import uvicorn
from schemas import TextPost
app = FastAPI()
text_posts = {
    1: TextPost(id=1, content="Hello, this is my first post!"),
    2: TextPost(id=2, content="FastAPI is great for building APIs!") 
}
@app.get("/posts")
def read_posts(limit: int = None):
    if limit is not None:
        return {"posts": list(text_posts.values())[:limit]}
    return text_posts


@app.get("/posts/{post_id}")
def read_post(post_id: int):
    return text_posts.get(post_id, {"error": "Post not found"})

@app.post("/posts") 
def create_post(post: TextPost) -> TextPost:
    text_posts[post.id] = post
    return {"message": "Post created successfully", "post": post}
