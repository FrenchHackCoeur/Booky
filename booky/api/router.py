from fastapi import APIRouter

from booky.api.books.controller import books_router

router = APIRouter()

router.include_router(books_router)


@router.get("/")
def home():
    return "Welcome to Booky API"
