# Facebook Post web scraper

This a facebook public page scraper created using Fastapi and Docker.
This api collects data from facebook pages and stores it in a mongodb database.


## Run this API

```bash
# Clone the repo
git clone https://github.com/salma-achour/facebook-scraper.git
cd facebook-scraper

# Install dependencies
pip install -r requirements.txt

# Run the api
uvicorn app.main:app --port 5000 --host 0.0.0.0
```
navigate to http://0.0.0.0:5000/docs


## Run with Docker
```bash
docker-compose up -d --build
```
navigate to http://0.0.0.0:5000/docs



## Run Tests with docker-compose
```bash
docker-compose exec scraper pytest .
```
