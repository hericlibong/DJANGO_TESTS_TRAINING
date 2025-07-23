
def test_is_classic_returns_true_for_classic_book(classic_book):
    assert classic_book.is_classic() is True

def test_is_classic_returns_false_for_modern_book(modern_book):
    assert modern_book.is_classic() is False

def test_is_long_returns_true_for_long_book(long_book):
    assert long_book.is_long() is True

def test_is_long_returns_false_for_short_book(short_book):
    assert short_book.is_long() is False

def test_classic_book_author_birth_year(classic_book):
    # classic_book est un Book dont l'auteur est classic_author
    assert classic_book.author.birth_year == 1920

def test_author_has_books(book_factory, classic_author):
    # Création de plusieurs livres pour le même auteur
    book_factory(title="A", author=classic_author)
    book_factory(title="B", author=classic_author)
    assert classic_author.book_set.count() == 2

def test_unknown_birth_author_is_handled_gracefully(unknown_birth_author):
    assert unknown_birth_author.birth_year is None

def test_modern_book_author_birth_year(modern_book):
    assert modern_book.author.birth_year == 1970

def test_contemporary_book_author_birth_year(contemporary_author):
    assert contemporary_author.birth_year == 1975


