from pydantic import BaseModel

class Website_Res(BaseModel):
    url: str
    status: str
    status_code: int | None
    response_time: int | None
    error: str | None