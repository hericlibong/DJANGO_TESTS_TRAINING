
def test_is_classic_returns_true_for_classic_book(classic_book):
    assert classic_book.is_classic() is True

def test_is_classic_returns_false_for_modern_book(modern_book):
    assert modern_book.is_classic() is False

def test_is_long_returns_true_for_long_book(long_book):
    assert long_book.is_long() is True

def test_is_long_returns_false_for_short_book(short_book):
    assert short_book.is_long() is False

# def test_book_factory_allows_custom_attributes(book_factory):
#     book = book_factory(title="Short Modern Book", published_year=2021, pages=99)
#     assert book.title == "Short Modern Book"
#     assert book.published_year == 2021
#     assert book.pages == 99
#     assert book.is_classic() is False
#     assert book.is_long() is False
