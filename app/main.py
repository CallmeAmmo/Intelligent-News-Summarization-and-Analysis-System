from api.endpoints import fetch_headline_news, fetch_sources, fetch_all_news
from database.db import get_database, update_db

params = {
    "q": "bitcoin",
    "language": "en",
    "from_param" : '2024-11-01',
    "to" : '2024-11-02',
    "sort_by": "relevancy",
    "page": 2
    }




news_data = fetch_all_news(params)
update_db(news_data)

