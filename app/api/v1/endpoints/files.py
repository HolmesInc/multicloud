from typing import Any
from fastapi import APIRouter

from app.api.v1 import schemas

router = APIRouter()


@router.post("/save", response_model=schemas.FileSave)
def save() -> Any:
    """
    Check application is up and running
    """

    return {"ping": "pong"}
