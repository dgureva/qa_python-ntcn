# qa_python_4
# В данном проекте написаны тесты для приложения BooksCollector.
# Описание тестов выглядит следующим образом:
TestBooksCollector.test_add_new_book_add_two_books: Проверяет возможность добавления двух новых книг в коллекцию.
TestBooksCollector.test_init_all_genre_exist: Этот тест включает несколько под-тестов для различных жанров: Фантастика, Ужасы, Детективы, Мультфильмы, Комедии. Каждый под-тест проверяет, что при инициализации коллекции все указанные жанры присутствуют.
TestBooksCollector.test_set_book_genre_genre_from_list_set_ok: Проверяет установку жанра книги, когда указанный жанр присутствует в допустимом списке жанров.
TestBooksCollector.test_set_book_genre_genre_out_of_list_not_set: Проверяет попытку установить жанр книги, который отсутствует в допустимом списке жанров.
TestBooksCollector.test_get_book_genre_return_genre_set: Проверяет корректность получения установленного жанра книги.
TestBooksCollector.test_get_books_with_specific_genre_get_two_books_the_same_genre_of_three: Проверяет получение книг с определенным жанром.
TestBooksCollector.test_get_books_for_children_get_one_book_without_age_rating_of_three: Проверяет получение детских книг, т.е. книг без возрастного ограничения.
TestBooksCollector.test_add_book_in_favorites_add_two_new_books: Проверяет добавление двух новых книг в список избранного.
TestBooksCollector.test_add_book_in_favorites_add_book_one_more_time_not_possible: Проверяет невозможность повторного добавления одной и той же книги в список избранного.
TestBooksCollector.test_add_book_in_favorites_add_book_out_of_list_not_possible: Проверяет невозможность добавления несуществующей книги в список избранного.
TestBooksCollector.test_delete_book_from_favorites_remove_one_book_possible: Проверяет возможность удаления книги из списка избранного.
TestBooksCollector.test_get_list_of_favorites_books_return_list_of_favorites_books_successfully: Проверяет корректность получения списка избранных книг.
# Все эти тесты помогают убедиться, что класс BooksCollector функционирует должным образом и обеспечивает корректное управление коллекцией книг, включая такие операции, как добавление, установка жанров, фиьтрация по жанрам, работа со списком избранного и многое другое.
