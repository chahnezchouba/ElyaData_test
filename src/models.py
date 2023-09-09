from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class FbPost(Base):
    __tablename__ = 'FbPosts'
    id  = Column(Integer, primary_key=True, index=True)
    time = Column(String) 
    text = Column(String)
    image = Column(String)
    likes = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)