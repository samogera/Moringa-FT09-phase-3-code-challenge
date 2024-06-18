from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ").strip()
    magazine_name = input("Enter magazine name: ").strip()
    magazine_category = input("Enter magazine category: ").strip()
    article_title = input("Enter article title: ").strip()
    article_content = input("Enter article content: ").strip()

    # Validate input length
    if not magazine_category:
        print("Magazine category cannot be empty.")
        return

    # Create Author, Magazine, and Article objects
    author = Author(name=author_name)
    magazine = Magazine(name=magazine_name, category=magazine_category)
    article = Article(title=article_title, content=article_content, author=author, magazine=magazine)

    # Save to database
    author.save()
    magazine.save()
    article.save()

    # Display inserted records
    print("\nMagazines:")
    for mag in Magazine.all_magazines():
        print(f"Magazine ID: {mag['id']}, Name: {mag['name']}, Category: {mag['category']}")

    print("\nAuthors:")
    for auth in Author.all_authors():
        print(f"Author ID: {auth['id']}, Name: {auth['name']}")

    print("\nArticles:")
    for art in Article.all_articles():
        print(f"Article ID: {art['id']}, Title: {art['title']}")

if __name__ == "__main__":
    main()
