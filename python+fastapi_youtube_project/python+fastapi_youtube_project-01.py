from fastapi import FastAPI
app = FastAPI()
@app.post("/")
def create_item(item: dict):
