import pytest
from main import BooksCollector


# ---------------- add_new_book ----------------
def test_add_new_book_adds_book_without_genre():
    collector = BooksCollector()
    collector.add_new_book('Метро 2033')
    assert collector.books_genre.get('Метро 2033') == ''


def test_add_new_book_does_not_add_if_name_too_long():
    collector = BooksCollector()
    long_name = 'А' * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.books_genre


@pytest.mark.parametrize('book_name', ['Город в огне', 'Тайна старого дома'])
def test_add_new_book_only_once(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_new_book(book_name)
    assert list(collector.books_genre.keys()).count(book_name) == 1


# ---------------- set_book_genre ----------------
def test_set_book_genre_sets_correct_genre():
    collector = BooksCollector()
    collector.add_new_book('Зулейха открывает глаза')
    collector.set_book_genre('Зулейха открывает глаза', 'Детективы')
    assert collector.books_genre['Зулейха открывает глаза'] == 'Детективы'


def test_set_book_genre_invalid_genre_not_set():
    collector = BooksCollector()
    collector.add_new_book('Тестовая книга')
    collector.set_book_genre('Тестовая книга', 'Фэнтези')  # нет в списке genre
    assert collector.books_genre['Тестовая книга'] == ''


# ---------------- get_book_genre ----------------
def test_get_book_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    assert collector.get_book_genre('Метро 2033') == 'Фантастика'


# ---------------- get_books_with_specific_genre ----------------
def test_get_books_with_specific_genre_returns_correct_list():
    collector = BooksCollector()
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    result = collector.get_books_with_specific_genre('Фантастика')
    assert result == ['Метро 2033']


# ---------------- get_books_genre ----------------
def test_get_books_genre_returns_full_dict():
    collector = BooksCollector()
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    assert collector.get_books_genre() == {'Метро 2033': 'Фантастика'}


# ---------------- get_books_for_children ----------------
def test_get_books_for_children_excludes_age_restricted():
    collector = BooksCollector()
    collector.add_new_book('Зулейха открывает глаза')
    collector.set_book_genre('Зулейха открывает глаза', 'Детективы')
    collector.add_new_book('Маленький принц')
    collector.set_book_genre('Маленький принц', 'Мультфильмы')
    result = collector.get_books_for_children()
    assert 'Маленький принц' in result and 'Зулейха открывает глаза' not in result


# ---------------- add_book_in_favorites ----------------
def test_add_book_in_favorites_adds_only_if_in_books():
    collector = BooksCollector()
    collector.add_new_book('Маленький принц')
    collector.add_book_in_favorites('Маленький принц')
    assert 'Маленький принц' in collector.favorites


def test_add_book_in_favorites_does_not_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Маленький принц')
    collector.add_book_in_favorites('Маленький принц')
    collector.add_book_in_favorites('Маленький принц')
    assert collector.favorites.count('Маленький принц') == 1


# ---------------- delete_book_from_favorites ----------------
def test_delete_book_from_favorites_removes_book():
    collector = BooksCollector()
    collector.add_new_book('Маленький принц')
    collector.add_book_in_favorites('Маленький принц')
    collector.delete_book_from_favorites('Маленький принц')
    assert 'Маленький принц' not in collector.favorites


# ---------------- get_list_of_favorites_books ----------------
def test_get_list_of_favorites_books_returns_list():
    collector = BooksCollector()
    collector.add_new_book('Маленький принц')
    collector.add_new_book('Метро 2033')
    collector.add_book_in_favorites('Маленький принц')
    collector.add_book_in_favorites('Метро 2033')
    assert collector.get_list_of_favorites_books() == ['Маленький принц', 'Метро 2033']
