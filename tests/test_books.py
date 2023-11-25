from pages.books import BookOperations
from library.config import TestData

book = TestData.book_id


def test_books():
    b = BookOperations()
    b.get_status()
    b.get_all_books()
    b.get_book(book)
