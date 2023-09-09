from facebook_scraper import get_posts
from contextlib import suppress

def scrape(page_name, page_limit):
    email = 'testscraping65@gmail.com'
    password = 'testtest789t'
    with suppress(Exception) :
        page_data=[]
        for post in get_posts(page_name, pages=page_limit, credentials=(email, password)):
            page_data.append({'time' : (post['time']),
                              'text' : post['text'][:200].isoformat(),
                              'image' : post['image'][:200],
                              'likes' : post['likes'],
                              'comments' : post['comments'],
                              'shares' : post['shares'],
                            })
    return page_data