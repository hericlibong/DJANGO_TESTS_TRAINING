import pytest
from core.models import Book


@pytest.fixture
def book_factory(db):
    """
    Factory fixture pour créer des instances de Book avec des paramètres personnalisables.
    
    Usage:
    - book_factory() : crée un livre avec des valeurs par défaut
    - book_factory(title="Mon Titre") : crée un livre avec un titre personnalisé
    - book_factory(published_year=1950, pages=500) : crée un livre avec année et pages personnalisées
    """
    def _create_book(
        title="Test Book", 
        author="Test Author", 
        published_year=2000, 
        pages=250
    ):
        return Book.objects.create(
            title=title,
            author=author,
            published_year=published_year,
            pages=pages
        )
    return _create_book


@pytest.fixture
def classic_book(book_factory):
    """Fixture pour créer un livre classique (publié avant 1980)."""
    return book_factory(
        title="Classic Literature",
        author="Classic Author", 
        published_year=1960,
        pages=200
    )


@pytest.fixture
def modern_book(book_factory):
    """Fixture pour créer un livre moderne (publié après 1980)."""
    return book_factory(
        title="Modern Novel",
        author="Modern Author",
        published_year=2020,
        pages=350
    )


@pytest.fixture
def long_book(book_factory):
    """Fixture pour créer un livre long (plus de 300 pages)."""
    return book_factory(
        title="Epic Tale",
        author="Prolific Author",
        published_year=1995,
        pages=450
    )


@pytest.fixture
def short_book(book_factory):
    """Fixture pour créer un livre court (300 pages ou moins)."""
    return book_factory(
        title="Short Story Collection",
        author="Concise Author",
        published_year=2010,
        pages=180
    )