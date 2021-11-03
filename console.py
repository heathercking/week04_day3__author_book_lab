import pdb

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


author_1 = Author("JK", "Rowling")
author_repository.save(author_1)
author_2 = Author("Stephen", "King")
author_repository.save(author_2)


book_1 = Book("Harry Potter", author_1, "Penguin Books", "2000")
book_repository.save(book_1)
book_2 = Book("IT", author_2, "Penguin Books", "1970")
book_repository.save(book_2)


pdb.set_trace()