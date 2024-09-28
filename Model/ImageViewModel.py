from datetime import datetime
from pydantic import BaseModel

class ImageViewModel(BaseModel):
    dateCreated: datetime
    filePath: str


