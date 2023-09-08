from fastapi import FastAPI, Query
from facebook_scraper import get_posts
from contextlib import suppress

email = 'testscraping65@gmail.com'
password = 'testtest789t'

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "WELCOME ! This is a Facebook-page scraping app."}

# Define a route for the scraping service
@app.get("/scrape/{page_name}")
async def scrape(page_name: str, page_limit: int  = Query(1)):
    with suppress(Exception) :
        page_data=[]
        for post in get_posts(page_name, pages=page_limit, credentials=(email, password)):
            page_data.append({'post_id' : post['post_id'],
                              'time' : (post['time']).isoformat(),
                              'text' : post['text'][:200],
                              'image' : post['image'][:200],
                              'likes' : post['likes'],
                              'comments' : post['comments'],
                              'shares' : post['shares'],
                            })
    return page_data
    

