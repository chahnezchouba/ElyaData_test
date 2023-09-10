from typing import Union
from pydantic import BaseModel
from datetime import datetime

class FbPosts(BaseModel):
    page_name : str
    time : datetime
    text : Union[str, None] = None
    image : Union[str, None] = None
    likes : Union[int, None] = None
    comments : Union[int, None] = None
    shares : Union[int, None] = None

    class Config:
        orm_mode = True