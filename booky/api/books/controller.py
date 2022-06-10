from fastapi import APIRouter, Depends

from booky.api.books.service import BooksService

books_router = APIRouter(prefix="/books")


@books_router.get("/")
def get_all_books(booksService: BooksService = Depends(BooksService)):
    return booksService.get_all_books()
