from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, publisher, publication_date) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.publisher, book.publication_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row["title"], author, row["publisher"], row["publication_date"], row["id"])
        books.append(author)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result["author_id"])
        book = Book(result["title"], author, result["publisher"], result["publication_date"], result["id"])
    return book