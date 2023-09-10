# Facebook Scrapping Service

This project is a Facebook scrapping service built using FastAPI. It scrapes public pages on Facebook and saves the data in a PostgreSQL database.
From each post, the app is designed to store the following attributes : page name, posting time, post text, image link, number of likes, number of comments and number of shares.

## Features

- Scrape a Facebook page
- Check the list of pages that were already scraped
- Check the content of the database

## How to run the app 

Both the service and the database are dockerized. To run the app, use the following command :
```bash
docker-compose up -d --build 
```
## Accessing the App
- Home page URL : `localhost:8000`
- Interactive API documentation URL : `localhost:8000/docs`

#### Available Routes : 
- `/scrape/{page_name}?page_limit={page_limit}` : to scrape a public page and save the data in the database by entreing the facebook page name. The limit page parameter is optional (default = 1).
- `/scraped_pages` : to get the list of pages names already scraped.
- `/saved_data` : to check the content of the database.

