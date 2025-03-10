from pydantic import BaseModel
from datetime import datetime

class TimeResponse(BaseModel):
    current_time: datetime
    timezone: str
