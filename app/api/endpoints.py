import os
from newsapi import NewsApiClient

api_key = os.getenv("NEWS_API_KEY")
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
    return top_headlines

def fetch_all_news(params):
    '''
        q='bitcoin',
        sources='bbc-news,the-verge',
        domains='bbc.co.uk,techcrunch.com',
        from_param='2017-12-01',
        to='2017-12-12',
        language='en',
        sort_by='relevancy',
        page=2
    '''

    all_articles = news_client.get_everything(**params)
    return all_articles


def fetch_sources():
    api_key = os.getenv("NEWS_API_KEY")

    print(api_key)
    news_client = NewsApiClient(api_key=api_key)

    sources = news_client.get_sources()
    return sources


