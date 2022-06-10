from fastapi import Depends
from sqlmodel import Session

from booky.data.dependencies import get_session


class BooksService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all_books(self):
        print("Test session", self.session)
        return ["Percy Jackson", "Hacker 2"]
