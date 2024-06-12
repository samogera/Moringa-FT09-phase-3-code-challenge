import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from database.setup import create_tables, get_db_connection

class TestModels(unittest.TestCase):

    def setUp(self):
        create_tables()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles')
        cursor.execute('DELETE FROM authors')
        cursor.execute('DELETE FROM magazines')
        conn.commit()
        conn.close()

    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsNotNone(author.id)

    def test_article_creation(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(title="Test Title", content="Test Content", author=author, magazine=magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.id, author.id)
        self.assertEqual(article.magazine.id, magazine.id)
        self.assertIsNotNone(article.id)

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsNotNone(magazine.id)

    def test_author_articles(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(title="Title 1", content="Content 1", author=author, magazine=magazine)
        Article(title="Title 2", content="Content 2", author=author, magazine=magazine)
        articles = author.articles()
        self.assertEqual(len(articles), 2)

    def test_author_magazines(self):
        author = Author("John Doe")
        magazine1 = Magazine("Tech Weekly", "Technology")
        magazine2 = Magazine("Health Monthly", "Health")
        Article(title="Title 1", content="Content 1", author=author, magazine=magazine1)
        Article(title="Title 2", content="Content 2", author=author, magazine=magazine2)
        magazines = author.magazines()
        self.assertEqual(len(magazines), 2)

    def test_magazine_articles(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(title="Title 1", content="Content 1", author=author, magazine=magazine)
        Article(title="Title 2", content="Content 2", author=author, magazine=magazine)
        articles = magazine.articles()
        self.assertEqual(len(articles), 2)

    def test_magazine_contributors(self):
        author1 = Author("John Doe")
        author2 = Author("Jane Smith")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(title="Title 1", content="Content 1", author=author1, magazine=magazine)
        Article(title="Title 2", content="Content 2", author=author2, magazine=magazine)
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 2)

    def test_magazine_article_titles(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(title="Title 1", content="Content 1", author=author, magazine=magazine)
        Article(title="Title 2", content="Content 2", author=author, magazine=magazine)
        titles = magazine.article_titles()
        self.assertEqual(len(titles), 2)
        self.assertIn("Title 1", titles)
        self.assertIn("Title 2", titles)

    def test_magazine_contributing_authors(self):
        author1 = Author("John Doe")
        author2 = Author("Jane Smith")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(title="Title 1", content="Content 1", author=author1, magazine=magazine)
        Article(title="Title 2", content="Content 2", author=author1, magazine=magazine)
        Article(title="Title 3", content="Content 3", author=author1, magazine=magazine)
        Article(title="Title 4", content="Content 4", author=author2, magazine=magazine)
        authors = magazine.contributing_authors()
        self.assertEqual(len(authors), 1)
        self.assertEqual(authors[0]['name'], "John Doe")

    def test_author_name_setter(self):
        author = Author("John Doe")
        author.name = "Jane Doe"
        self.assertEqual(author.name, "Jane Doe")
        with self.assertRaises(ValueError):
            author.name = ""

    def test_magazine_name_setter(self):
        magazine = Magazine("Tech Weekly", "Technology")
        magazine.name = "Health Monthly"
        self.assertEqual(magazine.name, "Health Monthly")
        with self.assertRaises(ValueError):
            magazine.name = "A"

    def test_magazine_category_setter(self):
        magazine = Magazine("Tech Weekly", "Technology")
        magazine.category = "Health"
        self.assertEqual(magazine.category, "Health")
        with self.assertRaises(ValueError):
            magazine.category = ""

    def test_article_content(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(title="Test Title", content="Test Content", author=author, magazine=magazine)
        self.assertEqual(article.content, "Test Content")

    def test_article_without_content(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        with self.assertRaises(TypeError):
            Article(title="Test Title", author=author, magazine=magazine)

    def test_duplicate_author_name(self):
        author1 = Author("John Doe")
        author2 = Author("John Doe")
        self.assertNotEqual(author1.id, author2.id)

    def test_duplicate_magazine_name(self):
        magazine1 = Magazine("Tech Weekly", "Technology")
        magazine2 = Magazine("Tech Weekly", "Health")
        self.assertNotEqual(magazine1.id, magazine2.id)

    def test_magazine_no_articles(self):
        magazine = Magazine("Tech Weekly", "Technology")
        articles = magazine.articles()
        self.assertEqual(len(articles), 0)

    def test_author_no_articles(self):
        author = Author("John Doe")
        articles = author.articles()
        self.assertEqual(len(articles), 0)

    def test_magazine_no_contributors(self):
        magazine = Magazine("Tech Weekly", "Technology")
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 0)

    def test_magazine_no_article_titles(self):
        magazine = Magazine("Tech Weekly", "Technology")
        titles = magazine.article_titles()
        self.assertIsNone(titles)

    def test_magazine_no_contributing_authors(self):
        magazine = Magazine("Tech Weekly", "Technology")
        authors = magazine.contributing_authors()
        self.assertIsNone(authors)

if __name__ == '__main__':
    unittest.main()
