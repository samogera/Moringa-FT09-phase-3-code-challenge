from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create Author, Magazine, and Article objects
    author = Author(author_name)
    magazine = Magazine(magazine_name, magazine_category)
    article = Article(article_title, article_content, author, magazine)

    # Display inserted records
    print("\nMagazines:")
    for mag in Magazine.all_magazines():
        print(mag)

    print("\nAuthors:")
    for auth in Author.all_authors():
        print(auth)

    print("\nArticles:")
    for art in Article.all_articles():
        print(art)

if __name__ == "__main__":
    main()
