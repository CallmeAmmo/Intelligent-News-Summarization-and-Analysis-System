import sqlite3
import pandas as pd
import os
from newspaper import Article
from tqdm import tqdm

def fetch_full_article_with_newspaper(url) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error extracting article: {e}")
        return None

def initialize_database() -> None:
    print('Initializing database...')

    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()

    query = """
            CREATE TABLE IF NOT EXISTS articles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                full_content TEXT,
                source_name TEXT,
                author TEXT,
                published_date TEXT,
                url TEXT UNIQUE NOT NULL, -- Unique URL to avoid duplicates
                description TEXT,
                urlToImage TEXT
            )
        """
    cursor.execute(query)

    conn.commit()
    conn.close()
    print("Database initialized with schema!\n")


def update_article(article) -> bool:
    conn =sqlite3.connect('news_data.db')
    curosr=conn.cursor()
    success = False

    try:
        query = """
                INSERT OR IGNORE INTO articles (title, content, full_content, source_name, author, published_date, url, description, urlToImage)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        curosr.execute(query, (
            article.get('title'),
            article.get('content'),
            article.get('full_content'),
            article.get('name'),
            article.get('author'),
            article.get('publishedAt'),
            article.get('url'),
            article.get('description'),
            article.get('urlToImage')
        ))

        if curosr.rowcount > 0:
            success = True

    except Exception as e:
        print(f"Error saving article in database: {e}")
    finally:
        conn.commit()
        conn.close()
    
    return success


def update_articles(processed_articles) -> int:
    cnt =0
    for i in tqdm(processed_articles):
        success = update_article(i)
        if success:
            cnt+=1

    return cnt

def update_db(news_data) -> None:
   
    if not os.path.exists('news_data.db'):
        print("Database does not exist!\n")
        initialize_database()
    
    print('Updating database...\n')

    articles = news_data.get('articles', [])
    processed_articles = []

    for i in articles:
        processed_article = {
            'name':i.get('source',{}).get('name', None),
            'author': i.get('author', None),
            'title': i.get('title', None),
            'description': i.get('description', None),
            'url': i.get('url', None),
            'urlToImage': i.get('urlToImage', None),
            'publishedAt': i.get('publishedAt', None),
            'content': i.get('content', None)
        }
    
        if processed_article.get('url'):
            # full_content = fetch_full_article_with_newspaper(processed_article.get('url'))
            full_content = processed_article.get('content')

            processed_article['full_content'] = full_content
            processed_articles.append(processed_article)
    
    arts_cnt = update_articles(processed_articles)
    print(f'Updated db with {arts_cnt} out of {len(processed_articles)} new articles')


def get_database(query) -> pd.DataFrame:
    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    conn.close()
    df = pd.DataFrame(rows, columns=columns)
    return df

