# FastAPI Blog Tutorial by Corey Schafer

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

fastapi-blog/
├── main.py              # FastAPI app entry point
├── config.py            # Configuration (SECRET_KEY, DB_URI)
├── database.py          # Database connection
├── models.py            # SQLAlchemy models (User, Post)
├── schemas.py           # Pydantic models (UserCreate, PostBase, etc.)
├── routers/             # FastAPI routes (auth, posts, users)
├── auth.py              # Authentication functions (JWT, password hashing)
├── image_utils.py       # Image processing (resize, save)
├── populate_db.py       # Populate database with sample data
├── templates/           # Jinja2 templates (optional — for email confirmation)
├── static/              # Static files (profile pictures, CSS, JS)
├── .env.example         # Environment template
├── .gitignore
├── pyproject.toml       # Dependencies (if using uv/poetry)
├── uv.lock              # uv lock file
└── README.md            # This file

## 🔐 Authentication Endpoints

* **POST /users/** — Register new user
* **POST /login** — Login and get access token
* **GET /users/me** — Get current user (requires token)
* **GET /users/{user_id}** — Get user by ID

#By Sneaky You can use this and share
