from fastapi import FastAPI , HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts ={
  "text_posts": {
    "1": {
      "title": "Introduction to Python",
      "content": "Python is a beginner-friendly programming language used for web development, automation, and data science."
    },
    "2": {
      "title": "Learning Software Testing",
      "content": "Software testing ensures that applications work correctly and meet user requirements."
    },
    "3": {
      "title": "Manual Testing Basics",
      "content": "Manual testing involves testing software manually without using automation tools."
    },
    "4": {
      "title": "Automation Testing",
      "content": "Automation testing uses scripts and tools like Selenium or Playwright to test applications automatically."
    },
    "5": {
      "title": "API Testing",
      "content": "API testing focuses on validating request and response data between systems."
    },
    "6": {
      "title": "Database Testing",
      "content": "Database testing verifies the integrity, consistency, and accuracy of data stored in databases."
    },
    "7": {
      "title": "Performance Testing",
      "content": "Performance testing checks how the system behaves under heavy load and stress."
    },
    "8": {
      "title": "Security Testing",
      "content": "Security testing identifies vulnerabilities like SQL Injection, XSS, and authentication flaws."
    },
    "9": {
      "title": "Continuous Integration",
      "content": "Continuous Integration helps developers merge code frequently and detect issues early."
    },
    "10": {
      "title": "DevOps Culture",
      "content": "DevOps encourages collaboration between development and operations teams for faster delivery."
    }
  }
}

@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
      return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id, {"error": "Post not found"})

@app.post("/posts")
def create_post(post: PostCreate):
    new_post= { "title": post.title, "content": post.content }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
