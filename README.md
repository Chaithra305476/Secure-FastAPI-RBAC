# Secure FastAPI RBAC

A backend API built with FastAPI that implements secure authentication using JWT (JSON Web Tokens) and Role-Based Access Control (RBAC). It supports access + refresh token flow, password hashing, and role-protected endpoints.

## Features

- User registration and login with hashed passwords (bcrypt)
- JWT-based authentication (access token + refresh token)
- Refresh token endpoint to renew access without re-login
- Role-Based Access Control (admin, manager, user) enforced via FastAPI dependencies
- PostgreSQL database with SQLAlchemy ORM
- Auto-generated interactive API docs (Swagger UI)

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Auth:** JWT (python-jose), bcrypt (passlib)
- **Server:** Uvicorn

## Project Structure
secure-api-rbac/
├── app/
│   ├── main.py            # App entry point
│   ├── core/
│   │   ├── config.py      # Environment variable settings
│   │   └── security.py    # Token creation, password hashing, role checks
│   ├── database/
│   │   ├── session.py     # DB connection & session
│   │   └── models.py      # SQLAlchemy models (User, RefreshToken)
│   ├── routers/
│   │   ├── auth.py        # Register, login, refresh endpoints
│   │   └── data_routes.py # Role-protected business endpoints
│   └── schemas/
│       └── schemas.py     # Pydantic request/response models
├── requirements.txt
└── .env                   # Environment variables (not committed)

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Chaithra305476/Secure-FastAPI-RBAC.git
cd Secure-FastAPI-RBAC
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/secure_api_db

### 5. Create the PostgreSQL database
```bash
createdb -U postgres secure_api_db
```

### 6. Run the server
```bash
uvicorn app.main:app --reload
```

### 7. Open the interactive docs
## API Endpoints

| Method | Endpoint             | Description                          | Auth Required |
|--------|----------------------|--------------------------------------|----------------|
| POST   | `/auth/register`     | Create a new user                    | No             |
| POST   | `/auth/login`        | Log in, receive access + refresh token | No           |
| POST   | `/auth/refresh`      | Get a new access token               | No (refresh token in body) |
| GET    | `/data/me`           | Get current logged-in user's info    | Yes            |
| GET    | `/data/admin-only`   | Admin-only protected route           | Yes (admin)    |
| GET    | `/data/manager-or-admin` | Manager or Admin protected route | Yes (manager/admin) |

## How Authentication Works

1. User registers via `/auth/register`
2. User logs in via `/auth/login` and receives:
   - An **access token** (short-lived, used for regular requests)
   - A **refresh token** (long-lived, used only to get new access tokens)
3. Protected routes require the access token in the `Authorization: Bearer <token>` header
4. When the access token expires, `/auth/refresh` issues a new one without requiring login again

## Author

Chaithra S — [GitHub](https://github.com/Chaithra305476) · [LinkedIn](https://linkedin.com/in/chaithrashivakanth)
