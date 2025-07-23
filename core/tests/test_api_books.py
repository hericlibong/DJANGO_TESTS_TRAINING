import pytest


@pytest.mark.django_db
def test_books_api_requires_authentication(api_client):
    response = api_client.get("/api/books/")
    assert response.status_code in (401, 403)   # DRF renvoie parfois 403 sur accès anonyme

@pytest.mark.django_db
def test_books_api_authenticated_access(authenticated_api_client):
    response = authenticated_api_client.get("/api/books/")
    assert response.status_code == 200




