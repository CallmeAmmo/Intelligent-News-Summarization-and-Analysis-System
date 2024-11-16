import sqlite3
import pandas as pd
import os

def initialie_database():

    db = os.path.exists('news_data.db')
    if db:
        print("Database already exists!")
        return

    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()

    query = """
            CREATE TABLE IF NOT EXISTS articles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
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
    print("Database initialized with schema!")


def update_article(article):
    conn =sqlite3.connect('news_data.db')
    curosr=conn.cursor()

    try:
        query = """
                INSERT OR IGNORE INTO article (title, content, source_name, author, published_date, url, description, urlToImage)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
        curosr.execute(query, (
            article.get('title'),
            article.get('content'),
            article.get('name'),
            article.get('author'),
            article.get('publishedAt'),
            article.get('url'),
            article.get('description'),
            article.get('urlToImage')
        ))
    except Exception as e:
        print(f"Error saving article in database: {e}")
    finally:
        conn.commit()
        conn.close()


def update_articles(processed_articles):

    for i in processed_articles:
        update_article(i)

def update_db(news_data):

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
            processed_articles.append(processed_article)
    
    update_articles(processed_articles)
    print(f'Updated db with {len(processed_articles)} new articles')


def get_database(query):
    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    conn.close()
    df = pd.DataFrame(rows, columns=columns)
    return df

if __name__ == "__main__":
    initialie_database()


