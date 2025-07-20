import pytest
from core.models import Book, Author


@pytest.fixture
def author_factory(db):
    """
    Factory fixture pour créer des instances d'Author avec des paramètres personnalisables.
    
    Usage:
    - author_factory() : crée un auteur avec des valeurs par défaut
    - author_factory(name="Jane Doe") : crée un auteur avec un nom personnalisé
    - author_factory(name="Tolkien", birth_year=1892) : crée un auteur avec nom et année de naissance
    """
    def _create_author(
        name="Test Author",
        birth_year=None
    ):
        return Author.objects.create(
            name=name,
            birth_year=birth_year
        )
    return _create_author


@pytest.fixture
def book_factory(db, author_factory):
    """
    Factory fixture pour créer des instances de Book avec des paramètres personnalisables.
    
    Usage:
    - book_factory() : crée un livre avec des valeurs par défaut
    - book_factory(title="Mon Titre") : crée un livre avec un titre personnalisé
    - book_factory(published_year=1950, pages=500) : crée un livre avec année et pages personnalisées
    - book_factory(author=author_instance) : crée un livre avec un auteur spécifique
    """
    def _create_book(
        title="Test Book", 
        author=None, 
        published_year=2000, 
        pages=250
    ):
        # Si aucun auteur n'est fourni, on en crée un par défaut
        if author is None:
            author = author_factory()
        
        return Book.objects.create(
            title=title,
            author=author,
            published_year=published_year,
            pages=pages
        )
    return _create_book


@pytest.fixture
def classic_book(book_factory, author_factory):
    """Fixture pour créer un livre classique (publié avant 1980)."""
    classic_author = author_factory(name="Classic Author", birth_year=1920)
    return book_factory(
        title="Classic Literature",
        author=classic_author, 
        published_year=1960,
        pages=200
    )


@pytest.fixture
def modern_book(book_factory, author_factory):
    """Fixture pour créer un livre moderne (publié après 1980)."""
    modern_author = author_factory(name="Modern Author", birth_year=1970)
    return book_factory(
        title="Modern Novel",
        author=modern_author,
        published_year=2020,
        pages=350
    )


@pytest.fixture
def long_book(book_factory, author_factory):
    """Fixture pour créer un livre long (plus de 300 pages)."""
    prolific_author = author_factory(name="Prolific Author", birth_year=1950)
    return book_factory(
        title="Epic Tale",
        author=prolific_author,
        published_year=1995,
        pages=450
    )


@pytest.fixture
def short_book(book_factory, author_factory):
    """Fixture pour créer un livre court (300 pages ou moins)."""
    concise_author = author_factory(name="Concise Author", birth_year=1980)
    return book_factory(
        title="Short Story Collection",
        author=concise_author,
        published_year=2010,
        pages=180
    )


# ========== Fixtures d'auteurs spécialisées ==========

@pytest.fixture
def classic_author(author_factory):
    """Fixture pour créer un auteur classique (né avant 1920)."""
    return author_factory(
        name="Charles Dickens",
        birth_year=1812
    )


@pytest.fixture
def modern_author(author_factory):
    """Fixture pour créer un auteur moderne (né après 1950)."""
    return author_factory(
        name="Haruki Murakami",
        birth_year=1949
    )


@pytest.fixture
def contemporary_author(author_factory):
    """Fixture pour créer un auteur contemporain (né après 1970)."""
    return author_factory(
        name="Elena Ferrante",
        birth_year=1975
    )


@pytest.fixture
def unknown_birth_author(author_factory):
    """Fixture pour créer un auteur sans année de naissance connue."""
    return author_factory(
        name="Anonymous Writer",
        birth_year=None
    )
