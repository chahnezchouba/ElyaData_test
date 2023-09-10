# Facebook Scrapping Service

This project is a Facebook scrapping service built using FastAPI. It scrapes public pages on Facebook and saves the data in a PostgreSQL database.

## Features

- Scrape a Facebook page
- Check the list of pages that were already scraped
- Check the content of the database

The app saves the following attributes from each post:

- Page name
- Posting time
- Post text
- Post image link
- Number of likes
- Number of comments
- Number of shares

## How to run the app :

Both the service and the database are dockerized. To run the app, use the following command:

```bash
docker-compose up -d --build

