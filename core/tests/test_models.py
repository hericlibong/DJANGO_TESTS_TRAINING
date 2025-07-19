import pytest
from core.models import Book

@pytest.mark.django_db
def test_is_classic_returns_true_for_old_books():
    book = Book.objects.create(title="Old Book", author="Author", published_year=1970)
    assert book.is_classic() is True

@pytest.mark.django_db
def test_is_classic_returns_false_for_new_books():
    book = Book.objects.create(title="New Book", author="Author", published_year=2020)
    assert book.is_classic() is False
