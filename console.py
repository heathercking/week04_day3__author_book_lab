import pdb

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("JK", "Rowling")
author_repository.save(author_1)
author_2 = Author("Stephen", "King")
author_repository.save(author_2)


book_1 = Book("Harry Potter", author_1, "Penguin Books", "2000")
book_repository.save(book_1)
book_2 = Book("IT", author_2, "Penguin Books", "1970")
book_repository.save(book_2)


for author in author_repository.select_all():
    print(author.__dict__)

author = author_repository.select(author_1.id)
print(author.__dict__)

for book in book_repository.select_all():
    print(book.__dict__)

book = book_repository.select(book_1.id)
print(book.__dict__)

# book_repository.delete(book_1.id)
# author_repository.delete(author_1.id)


pdb.set_trace()