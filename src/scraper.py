from facebook_scraper import get_posts
from contextlib import suppress


def scrape(page_name, page_limit):
    email = 'chaimascrap@gmail.com'
    password = 'chaima789/'
    page_data=[]
    
    for post in get_posts(page_name, pages=page_limit, credentials=(email, password)):
        with suppress(Exception) :
            page_data.append({'page_name' : page_name,
                              'time' : (post['time'].isoformat()),
                              'text' : post['text'][:200],
                              'image' : post['image'][:200],
                              'likes' : post['likes'],
                              'comments' : post['comments'],
                              'shares' : post['shares']
                              })

    return page_data

