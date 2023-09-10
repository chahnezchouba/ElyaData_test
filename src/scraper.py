import facebook_scraper
from contextlib import suppress

EMAIL = 'chaimascrap@gmail.com'
PASSWORD = 'chaima789/'


def scrape(page_name, page_limit):
    page_data=[]
    posts = facebook_scraper.get_posts(page_name, 
                                       pages=page_limit, 
                                       credentials=(EMAIL, PASSWORD))
    for post in posts:
        with suppress(Exception) :
            page_data.append({'page_name' : page_name,
                              'time' : (post['time']),
                              'text' : post['text'][:200],
                              'image' : post['image'][:200],
                              'likes' : post['likes'],
                              'comments' : post['comments'],
                              'shares' : post['shares']
                              })

    return page_data

