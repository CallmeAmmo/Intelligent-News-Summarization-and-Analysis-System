from db import get_database


if __name__ == "__main__":
    df = get_database("SELECT * FROM articles")
    print(df)
    print(df.info())
    print(df.shape)