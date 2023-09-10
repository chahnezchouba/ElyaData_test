from fastapi import  Depends, FastAPI, Query
from sqlalchemy.orm import Session, defer
from sqlalchemy import  text

from database import SessionLocal, engine, Base
from models import FbPost
from scraper import scrape



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Facebook pages scraper")

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

@app.get('/scraped_pages')
async def get_scraped_pages_names(db: Session = Depends(get_db)):
    page_names = set([post.page_name for post in db.query(FbPost).all()])
    return page_names
    
@app.get('/saved_data')
async def check_data(db: Session = Depends(get_db)):
    data = db.query(FbPost).all()
    return data


