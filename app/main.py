from api.endpoints import fetch_headline_news, fetch_sources, fetch_all_news, fetch_news_today
from database.db import get_database, update_db


news_data_today = fetch_news_today('bitcoin')
update_db(news_data_today)

