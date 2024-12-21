import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Зов Ктулху')
        collector.add_new_book('Паддингтон')
        assert len(collector.books_genre) == 3

    def test_add_new_book_add_books_without_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_again(self, create_new_book):
        create_new_book.add_new_book('Властелин колец')
        assert len(create_new_book.get_books_genre()) == 1

    def test_add_new_book_add_book_over_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмные начала: Северный огонь Филип Пулман')
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_all_genre_exist(self, genre):
        collector = BooksCollector()
        assert genre in collector.genre

    def test_set_book_genre_set_real_genre(self, create_new_book):
        create_new_book.set_book_genre('Властелин колец', 'Фантастика')
        assert create_new_book.get_book_genre('Властелин колец') == f'Фантастика'

    def test_set_book_genre_set_unreal_genre(self, create_new_book):
        create_new_book.set_book_genre('Властелин колец', 'Фэнтези')
        assert create_new_book.books_genre != {'Властелин колец': 'Фэнтези'}

    def test_set_book_genre_set_genre_without_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.books_genre != {'Властелин колец': 'Фантастика'}


    def test_get_book_genre_book_without_genre(self, create_new_book):
        assert create_new_book.get_book_genre('Властелин колец') == f''


    def test_get_books_with_specific_genre_real_genre(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_with_specific_genre('Фантастика') == ['Властелин колец']

    def test_get_books_with_specific_genre_without_books(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_with_specific_genre('Детективы') == []


    def test_get_books_for_children_child_rating(self, create_new_books_with_genres):
        assert create_new_books_with_genres.get_books_for_children() == ['Властелин колец']

    def test_get_books_for_children_without_books(self):
        collector = BooksCollector()
        collector.add_new_book('Зов Ктулху')
        collector.set_book_genre('Зов Ктулху', 'Ужасы')
        assert collector.get_books_for_children() == []


    def test_add_book_in_favorites_real_book(self, create_new_book):
        create_new_book.add_book_in_favorites('Властелин колец')
        assert create_new_book.get_list_of_favorites_books() == ['Властелин колец']

    def test_add_book_in_favorites_add_book_again(self, create_new_book):
        create_new_book.add_book_in_favorites('Властелин колец')
        create_new_book.add_book_in_favorites('Властелин колец')
        assert create_new_book.favorites == ['Властелин колец']

    def test_add_book_in_favorites_unreal_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Паддингтон')
        assert collector.favorites == []


    def test_delete_book_from_favorites_real_book(self, create_new_book):
        create_new_book.add_book_in_favorites('Властелин колец')
        create_new_book.delete_book_from_favorites('Властелин колец')
        assert create_new_book.favorites == []

    def test_delete_book_from_favorites_unreal_book(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Паддингтон')
        assert collector.favorites == []


    def test_get_list_of_favorites_books_empty_list(self, create_new_book):
        assert create_new_book.favorites == []

    def test_get_books_genre_collection_returned(self, create_new_books_with_genres):
        collector = create_new_books_with_genres
        result = collector.get_books_genre()
        expected_result = {
            'Властелин колец': 'Фантастика',
            'Зов Ктулху': 'Ужасы'
        }
        assert result == expected_result
