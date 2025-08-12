# BooksCollector Tests

В проекте реализованы автотесты для класса `BooksCollector`.

## Покрытие тестами

### 1. add_new_book
- **test_add_new_book_adds_book_without_genre** — проверяет, что новая книга (`Метро 2033`) добавляется в словарь без жанра.
- **test_add_new_book_does_not_add_if_name_too_long** — проверяет, что книга с названием длиной более 40 символов не добавляется.
- **test_add_new_book_only_once** *(параметризованный)* — проверяет, что книги (`Город в огне`, `Тайна старого дома`) не добавляются повторно.

### 2. set_book_genre
- **test_set_book_genre_sets_correct_genre** — проверяет установку корректного жанра (`Детективы`) для книги `Зулейха открывает глаза`.
- **test_set_book_genre_invalid_genre_not_set** — проверяет, что жанр, которого нет в списке допустимых, не устанавливается.

### 3. get_books_with_specific_genre
- **test_get_books_with_specific_genre_returns_correct_list** — проверяет, что метод возвращает список книг (`Метро 2033`) с определённым жанром (`Фантастика`).

### 4. get_books_for_children
- **test_get_books_for_children_excludes_age_restricted** — проверяет, что книги с возрастным рейтингом (`Зулейха открывает глаза`, жанр `Детективы`) не попадают в список детских, а книги без возрастного рейтинга (`Маленький принц`, жанр `Мультфильмы`) — попадают.

### 5. add_book_in_favorites
- **test_add_book_in_favorites_adds_only_if_in_books** — проверяет, что в избранное можно добавить только книгу, которая есть в словаре (`Маленький принц`).
- **test_add_book_in_favorites_does_not_duplicate** — проверяет, что повторное добавление той же книги (`Маленький принц`) не создаёт дублей.

### 6. delete_book_from_favorites
- **test_delete_book_from_favorites_removes_book** — проверяет, что книга (`Маленький принц`) удаляется из списка избранного.

### 7. get_list_of_favorites_books
- **test_get_list_of_favorites_books_returns_list** — проверяет, что метод возвращает полный список избранных книг (`Маленький принц`, `Метро 2033`).

---

## Запуск тестов
Для запуска тестов используйте команду:
```bash
pytest -v tests.py
