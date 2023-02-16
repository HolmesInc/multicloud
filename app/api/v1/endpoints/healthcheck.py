from typing import Any
from fastapi import APIRouter

from app.api.v1 import schemas

router = APIRouter()


@router.get("/", response_model=schemas.Healthcheck)
def healthcheck() -> Any:
    """
    Check application is up and running
    """

    return {"ping": "pong"}
