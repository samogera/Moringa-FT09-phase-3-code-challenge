import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Creates tables for authors, magazines, and articles in the SQLite database."""
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Define table creation queries
    table_queries = [
        '''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
        )
        '''
    ]

    try:
        # Execute each table creation query
        for query in table_queries:
            cursor.execute(query)

        # Commit changes and close connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

