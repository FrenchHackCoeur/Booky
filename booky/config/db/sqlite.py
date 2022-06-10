from typing import Literal, Optional

from confz import ConfZ


class SQLiteConfig(ConfZ):
    type: Literal["sqlite"]
    path: Optional[str]  # None if the db is in memory
