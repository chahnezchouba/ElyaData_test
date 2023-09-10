from unittest.mock import patch
from datetime import datetime
import facebook_scraper

from src.scraper import scrape


@patch('facebook_scraper.get_posts') 
def test_scrape_function(mock_get_posts):
    mock_get_posts.return_value = [{'post_id': '1234567890123456789',
                                    'text': 'This is an example Facebook post!',
                                    'post_text': 'This is an example Facebook post!',
                                    'shared_text': '',
                                    'time': datetime(2022, 4, 7, 19, 50, 9),
                                    'image': 'https://facebook.com/image/url',
                                    'likes': 123,
                                    'comments': 20,
                                    'shares': 15,
                                    'post_url': 'https://facebook.com/post/url',
                                    'link': None
                                    },]
            
    assert scrape('ScrapTest', 4) == [{'page_name' : 'ScrapTest',
                                            'time': datetime(2022, 4, 7, 19, 50, 9),
                                            'text': 'This is an example Facebook post!',
                                            'image' : 'https://facebook.com/image/url',
                                            'likes' : 123,
                                            'comments' : 20,
                                            'shares' : 15
                                            },]
    
    assert scrape('ScrapTest', 4) == [{'page_name' : 'Scrap',
                                            'time': datetime(2022, 4, 7, 19, 50, 9),
                                            'text': 'This is an example Facebook post!',
                                            'image' : 'https://facebook.com/image/url',
                                            'likes' : 123,
                                            'comments' : 20,
                                            'shares' : 15
                                            },]

test_scrape_function()

