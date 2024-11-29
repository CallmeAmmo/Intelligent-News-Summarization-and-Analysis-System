import os
import datetime
from newsapi import NewsApiClient

api_key = os.getenv("NEWS_API_KEY")

if api_key is None:
    raise Exception("News API key is not set")

news_client = NewsApiClient(api_key=api_key)

def fetch_headline_news(params):
    '''
        q='bitcoin',
        sources='bbc-news,the-verge',
        category='business',
        language='en',
        country='us'

        Source param can not be present with category or country params
    '''

    top_headlines = news_client.get_top_headlines(**params)
    print('Data of Top Headlines fetched from news api')
    return top_headlines

def fetch_all_news(params):
    '''
        q='bitcoin',
        sources='bbc-news,the-verge',    #optional
        domains='bbc.co.uk,techcrunch.com', #optional
        from_param='2024-12-01',
        to='2024-12-12',
        language='en',
        sort_by='relevancy',
        page=2
    '''

    all_articles = news_client.get_everything(**params)
    print('Data for all news fetched from news api')
    return all_articles


def fetch_sources():
    api_key = os.getenv("NEWS_API_KEY")

    print(api_key)
    news_client = NewsApiClient(api_key=api_key)

    sources = news_client.get_sources()
    print('Data of Sources fetched from news api')
    return sources


def fetch_news_today(query):

    dt_today = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    print(f'Fetching news data for {dt_today} ........\n')
    params = {
        "q": query,
        "language": "en",
        "from_param" : dt_today,
        "to" : dt_today,
        "sort_by": "relevancy",
        "page": 1
        }
    
    news_data = fetch_all_news(params)
    return news_data



