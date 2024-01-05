from datetime import datetime, timezone
from pydantic import BaseModel



class OperationCreate(BaseModel):
    quantity: str
    figi: str
    instrument_type: str
    date: datetime = datetime.now(timezone.utc)
    type: str

    class Config:
        from_attributes = True

