from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from app.core.db import create_db_and_tables, get_session
from app.models.models import User
from app.api import auth

app = FastAPI(title="College LMS API")

# Инициализация БД при старте
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to College LMS API", "status": "working"}