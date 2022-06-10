from sqlmodel import Session

from booky.data import engine


def get_session():
    with Session(engine) as session:
        yield session
