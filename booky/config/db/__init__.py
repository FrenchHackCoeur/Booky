from typing import Union

from confz import ConfZ, ConfZEnvSource, ConfZFileSource

from booky.config import APP_ENVIRONMENT, CONFIG_DIR
from booky.config.db.postgres import PostgresConfig
from booky.config.db.sqlite import SQLiteConfig

DB_CONFIG_DIR = CONFIG_DIR / "db"

DBTypes = Union[SQLiteConfig, PostgresConfig]


class DBConfig(ConfZ):
    echo: bool
    db: DBTypes

    CONFIG_SOURCES = [
        ConfZFileSource(
            file=DB_CONFIG_DIR / f"db_{APP_ENVIRONMENT}.yaml"
        ),
        ConfZEnvSource(
            allow=[
                "DB_USER",
                "DB_PASSWORD"
            ],
            remap={
                "DB_USER": "db.user",
                "DB_PASSWORD": "db.password"
            }
        )
    ]
