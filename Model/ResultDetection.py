from datetime import datetime
from pydantic import BaseModel

class ResultDetection(BaseModel):
    dateCreated: datetime
    imageName: str
    result: str
