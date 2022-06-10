from sqlalchemy.engine import URL
from sqlmodel import create_engine

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgrespw",
    host="localhost",
    database="postgres"
)

engine = create_engine(url)

