from fastapi import  Depends, FastAPI, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from models import FbPost
from scraper import scrape
from database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return {"Message": "WELCOME ! This is a Facebook-page scraping app."}


# Define a route for the scraping service
@app.get("/scrape/{page_name}")
async def scraping(page_name: str, 
                   page_limit: int  = Query(1), 
                   db: Session = Depends(get_db)):
  
    try :
        posts = scrape(page_name, page_limit)
        db.bulk_insert_mappings(FbPost, posts)
        db.commit()
        return "page scraped"
    
    except Exception as e :
        return str(e)
    
@app.get('/pages')
async def check_data(db: Session = Depends(get_db)):
    pages = db.query(FbPost).all()
    return pages


