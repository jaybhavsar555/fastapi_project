from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Your data
posts = [
    {"id": 1, "author": "Jay Bhavsar", "title": "First Post", "content": "This is the first post.", "date_posted": datetime(2026, 3, 1)},
    {"id": 2, "author": "Jay Bhavsar", "title": "Second Post", "content": "This is the second post.", "date_posted": datetime(2026, 3, 2)},
    {"id": 3, "author": "Jay Bhavsar", "title": "Third Post", "content": "This is the third post.", "date_posted": datetime(2026, 3, 3)}
]

# Health check (Railway requirement)
@app.get("/health")
def health():
    return {"status": "healthy"}

# API endpoint
@app.get("/api/posts")
def get_posts():
    return posts

# Home page (FIXED TemplateResponse)
@app.get("/", include_in_schema=False, name="home", response_class=HTMLResponse)
@app.get("/posts", include_in_schema=False, name="posts", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,  # REQUIRED for Jinja2 url_for()
            "posts": posts,
            "title": "Home Page"
        }
    )
