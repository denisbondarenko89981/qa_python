import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


# ---------------- add_new_book ----------------
def test_add_new_book_adds_book_without_genre(collector):
    collector.add_new_book("Метро 2033")
    assert collector.get_books_genre() == {"Метро 2033": ""}


def test_add_new_book_does_not_add_if_name_too_long(collector):
    long_name = "А" * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()


@pytest.mark.parametrize("book", ["Город в огне", "Тайна старого дома"])
def test_add_new_book_only_once(collector, book):
    collector.add_new_book(book)
    collector.add_new_book(book)
    assert list(collector.get_books_genre().keys()).count(book) == 1


# ---------------- set_book_genre ----------------
def test_set_book_genre_sets_correct_genre(collector):
    collector.add_new_book("Зулейха открывает глаза")
    collector.set_book_genre("Зулейха открывает глаза", "Детективы")
    assert collector.get_book_genre("Зулейха открывает глаза") == "Детективы"


def test_set_book_genre_invalid_genre_not_set(collector):
    collector.add_new_book("Метро 2033")
    collector.set_book_genre("Метро 2033", "Фэнтези")  # такого жанра нет
    assert collector.get_book_genre("Метро 2033") == ""


# ---------------- get_books_with_specific_genre ----------------
def test_get_books_with_specific_genre_returns_correct_list(collector):
    collector.add_new_book("Метро 2033")
    collector.add_new_book("Город в огне")
    collector.set_book_genre("Метро 2033", "Фантастика")
    collector.set_book_genre("Город в огне", "Ужасы")
    result = collector.get_books_with_specific_genre("Фантастика")
    assert result == ["Метро 2033"]


# ---------------- get_books_for_children ----------------
def test_get_books_for_children_excludes_age_restricted(collector):
    collector.add_new_book("Зулейха открывает глаза")
    collector.add_new_book("Маленький принц")
    collector.set_book_genre("Зулейха открывает глаза", "Детективы")  # возрастное ограничение
    collector.set_book_genre("Маленький принц", "Мультфильмы")         # без возрастного ограничения
    result = collector.get_books_for_children()
    assert result == ["Маленький принц"]


# ---------------- add_book_in_favorites ----------------
def test_add_book_in_favorites_adds_only_if_in_books(collector):
    collector.add_new_book("Маленький принц")
    collector.add_book_in_favorites("Маленький принц")
    assert collector.get_list_of_favorites_books() == ["Маленький принц"]


def test_add_book_in_favorites_does_not_duplicate(collector):
    collector.add_new_book("Маленький принц")
    collector.add_book_in_favorites("Маленький принц")
    collector.add_book_in_favorites("Маленький принц")
    assert collector.get_list_of_favorites_books().count("Маленький принц") == 1


# ---------------- delete_book_from_favorites ----------------
def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book("Маленький принц")
    collector.add_book_in_favorites("Маленький принц")
    collector.delete_book_from_favorites("Маленький принц")
    assert "Маленький принц" not in collector.get_list_of_favorites_books()


# ---------------- get_list_of_favorites_books ----------------
def test_get_list_of_favorites_books_returns_list(collector):
    collector.add_new_book("Маленький принц")
    collector.add_new_book("Метро 2033")
    collector.add_book_in_favorites("Маленький принц")
    collector.add_book_in_favorites("Метро 2033")
    result = collector.get_list_of_favorites_books()
    assert result == ["Маленький принц", "Метро 2033"]
