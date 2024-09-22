# Sprint_4
    1) тест добаляет книгу с правильным названием в словарь 
    test_add_new_book_right_name(self)

    2) тестирует код на добавление слишком длинного названия
    test_add_new_book_name_more(self):

    3) тест на установку жанра книги, если такой жанр существует в списке жанров
    test_set_book_genre_in_genre_true(self):

    4) тест на неустановку жанра книги, если такой жанр не существует в списке жанров
    test_set_book_genre_in_genre_false(self):

    5) тест на получение жанра книги по ее имени
    test_get_book_genre_in_genre(self):

    6) тестируется метод вывода списка книг с определённым жанром
    test_get_books_with_specific_genre(self):

    7) параметризированный тест, который проверяет возвращение жанра книги по имени  
    @pytest.mark.parametrize('name', ['Бегущий по лезвию 2049', 'Евротур'])
        def test_get_book_genre_in_genre_true(self, name):

    8) тестируем метод вывода списка книг, подходящие детям
    test_get_books_for_children_true(self):

    9) тест метода добавления книги в избранное
    test_add_book_in_favorites_true(self):

    10) тест метода удаления книги из избранного 
    test_delete_book_from_favorites_true(self):

    11) тест метода получения списка избранных книг 
    test_get_list_of_favorites_books(self):
