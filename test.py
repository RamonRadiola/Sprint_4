import pytest

from main import BooksCollector

from data import book_names
from data import genre_names

class TestBooksCollector:
    def test_add_new_book_right_name(self):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_names[0])
        assert books_collector.books_genre == {'Бегущий по лезвию 2049': ''}

    def test_add_new_book_name_more(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('siaueyhbgpowierubpasoierubq[opweitnj[qpietq[wsgwegwedgwkujhqliuehliuerghikjdfhgksjdfhgksjdfhglsakdfjghslkdjfghlakdjfghlakdjfhkjrhgksjhfdgkjshdfkjghskjhdfgksjdhfgksjdhfkgjh')
        assert books_collector.books_genre == {}

    def test_set_book_genre_in_genre_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_names[0])
        books_collector.set_book_genre(book_names[0], genre_names[0])
        assert books_collector.books_genre == {'Бегущий по лезвию 2049': 'Фантастика'}

    def test_set_book_genre_in_genre_false(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.set_book_genre('Бегущий по лезвию 2049', 'Приключения')
        assert books_collector.books_genre != {'Бегущий по лезвию 2049', 'Приключения'}

    def test_get_book_genre_in_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Евротур')
        books_collector.set_book_genre('Бегущий по лезвию 2049', 'Фантастика')
        books_collector.set_book_genre('Евротур', 'Комедии')
        assert books_collector.get_book_genre('Бегущий по лезвию 2049') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Евротур')
        books_collector.add_new_book('Такси')
        books_collector.set_book_genre('Бегущий по лезвию 2049', 'Фантастика')
        books_collector.set_book_genre('Евротур', 'Комедии')
        books_collector.set_book_genre('Такси', 'Комедии')
        assert books_collector.get_books_with_specific_genre('Комедии') == ['Евротур', 'Такси']

    @pytest.mark.parametrize('name', ['Бегущий по лезвию 2049', 'Евротур'])
    def test_get_book_genre_in_genre_true(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Евротур')
        books_collector.set_book_genre('Бегущий по лезвию 2049', 'Фантастика')
        books_collector.set_book_genre('Евротур', 'Комедии')
        assert books_collector.get_book_genre(name) == books_collector.books_genre.get(name)


    def test_get_books_for_children_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Чужой')
        books_collector.add_new_book('Такси')
        books_collector.set_book_genre('Бегущий по лезвию 2049', 'Фантастика')
        books_collector.set_book_genre('Чужой', 'Ужасы')
        books_collector.set_book_genre('Такси', 'Комедии')
        assert books_collector.get_books_for_children() == ['Бегущий по лезвию 2049', 'Такси']

    def test_add_book_in_favorites_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Чужой')
        books_collector.add_new_book('Такси')
        books_collector.add_book_in_favorites('Бегущий по лезвию 2049')
        books_collector.add_book_in_favorites('Такси')
        assert books_collector.favorites == ['Бегущий по лезвию 2049', 'Такси']

    def test_delete_book_from_favorites_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Чужой')
        books_collector.add_new_book('Такси')
        books_collector.add_book_in_favorites('Бегущий по лезвию 2049')
        books_collector.add_book_in_favorites('Такси')
        books_collector.delete_book_from_favorites('Такси')
        assert books_collector.favorites == ['Бегущий по лезвию 2049']

<<<<<<< HEAD
    def test_get_list_of_favorites_books_true(self):
=======
    def test_get_list_of_favorites_books(self):
>>>>>>> origin/develop
        books_collector = BooksCollector()
        books_collector.add_new_book('Бегущий по лезвию 2049')
        books_collector.add_new_book('Чужой')
        books_collector.add_new_book('Такси')
        books_collector.add_book_in_favorites('Бегущий по лезвию 2049')
        books_collector.add_book_in_favorites('Такси')
        books_collector.delete_book_from_favorites('Такси')
<<<<<<< HEAD
        assert books_collector.get_list_of_favorites_books() == ['Бегущий по лезвию 2049']
=======
        books_collector.delete_book_from_favorites('Бегущий по лезвию 2049')
        assert books_collector.favorites == []
>>>>>>> origin/develop
