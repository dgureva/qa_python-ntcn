import pytest
from main import BooksCollector


@pytest.fixture
def collector_book():
    collector_book = BooksCollector()
    collector_book.add_new_book('Гордость и предубеждение и зомби')
    collector_book.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector_book.add_new_book('It')
    collector_book.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector_book.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    collector_book.set_book_genre('It', 'Комедии')
    return collector_book
