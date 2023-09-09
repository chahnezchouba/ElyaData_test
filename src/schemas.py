from pydantic import BaseModel
from datetime import datetime

class FbPosts(BaseModel):
    time : str
    text : str
    image : str
    likes : int
    comments : int
    shares : int

    class Config:
        orm_mode = True