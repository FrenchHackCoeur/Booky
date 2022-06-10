from confz import ConfZ, ConfZFileSource

from booky.config import CONFIG_DIR


class APIConfig(ConfZ):
    title: str
    description: str
    version: str

    CONFIG_SOURCES = ConfZFileSource(file=CONFIG_DIR / "api.yaml")
