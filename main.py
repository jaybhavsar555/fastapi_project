from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI live on Railway!", "posts": [{"id":1,"title":"First Post"}]}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/posts")
def get_posts():
    return [{"id":1,"title":"First Post"}]
