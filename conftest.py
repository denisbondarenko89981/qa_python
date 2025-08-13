import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Фикстура для создания нового объекта BooksCollector перед каждым тестом"""
    return BooksCollector()
