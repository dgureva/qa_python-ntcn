import pytest
from main import BooksCollector

@pytest.fixture
def create_new_book():
    collector = BooksCollector()
    collector.add_new_book('Властелин колец')
    return collector

@pytest.fixture
def create_new_books_with_genres():
    collector = BooksCollector()
    collector.add_new_book('Властелин колец')
    collector.set_book_genre('Властелин колец', 'Фантастика')
    collector.add_new_book('Зов Ктулху')
    collector.set_book_genre('Зов Ктулху', 'Ужасы')
    return collector
