# FastAPI (My first FastAPI)

to build a full-stack API with user authentication, database models, and CRUD operations — using **FastAPI**, **SQLAlchemy**, **Pydantic**, and **uv**.

## 🎯 What You'll Find Here

- ✅ **FastAPI** with automatic Swagger UI and ReDoc
- ✅ **SQLAlchemy ORM** for database operations
- ✅ **Pydantic models** for request/response validation
- ✅ **JWT authentication** (login, token refresh)
- ✅ User registration and login endpoints
- ✅ Post creation, editing, and deletion
- ✅ Profile pictures and image uploads
- ✅ Pagination and search
- ✅ Environment variables with `.env`
- ✅ `uv` for dependency management (not `pip` or `venv`)
- ✅ `templates/` for Jinja2 (optional — for email confirmation or admin pages)
- ✅ `static/` for profile pictures and static assets

## 🚀 How to Run

1. Clone the repo:
   ```bash
   https://github.com/sneaky91/FastAPI-myfirstAPI-.git

# before go to the website you need to do this
 Go to terminal in vscode or pycharm and do this bash script
--- 👌 uv run fastapi dev main.py

# You have website 
https://localhost:8000/ -- this a website
## or 
http://127.0.0.1:8000/

# And you have FastAPI-Swagger UI
https://localhost:8000/docs
## or
http://127.0.0.1:8000/


## 🔐 Authentication Endpoints

* **POST /users/** — Register new user
* **POST /login** — Login and get access token
* **GET /users/me** — Get current user (requires token)
* **GET /users/{user_id}** — Get user by ID

# By Sneaky You can use this and share
