# models/article.py
import sqlite3
from database.connection import get_db_connection

class Article:
    def __init__(self, title, content, author, magazine):
        self._title = title
        self._content = content
        self._author_id = author.id
        self._magazine_id = magazine.id
        self._id = None

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (self._title, self._content, self._author_id, self._magazine_id)
        )
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content must be a non-empty string")
        self._content = value

    @classmethod
    def all_articles(cls):
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        conn.close()
        return articles
