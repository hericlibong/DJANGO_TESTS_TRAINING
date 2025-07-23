def test_classic_books_count(book_factory, author_factory):
    # On crée un auteur
    author = author_factory(name="Classic Writer", birth_year=1930)
    # On lui crée deux livres "classiques"
    book_factory(title="Old 1", author=author, published_year=1970)
    book_factory(title="Old 2", author=author, published_year=1965)
    # Et un livre moderne
    book_factory(title="Modern", author=author, published_year=2005)

    # Testons la méthode métier
    assert author.classic_books_count() == 2
