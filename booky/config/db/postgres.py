from typing import Literal

from confz import ConfZ
from pydantic import SecretStr


class PostgresConfig(ConfZ):
    type: Literal["postgres"]
    user: str
    password: SecretStr
    host: str
    port: int
    database: str
