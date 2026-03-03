from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts : list[dict] = [
    {"id": 1, "author" : "Jay Bhavsar" ,"title": "First Post", "content": "This is the first post."},
    {"id": 2, "author" : "Jay Bhavsar" ,"title": "Second Post", "content": "This is the second post."},
    {"id": 3, "author" : "Jay Bhavsar" ,"title": "Third Post", "content": "This is the third post."}
    
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request : Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title":"Home Page"})


@app.get("/api/posts")
def get_posts():
    return posts