from fastapi import FastAPI

from booky.api.router import router
from booky.config.api import APIConfig


def create_booky_api() -> FastAPI:
    api = FastAPI(
        title=APIConfig().title,
        description=APIConfig().description,
        version=APIConfig().version
    )

    api.include_router(router)

    return api
