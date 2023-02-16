from pydantic import BaseModel


class Healthcheck(BaseModel):
    ping: str
