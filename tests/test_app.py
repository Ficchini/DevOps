from app import app

def test_home():
    client = app.test_client()
    assert client is not None
    response = client.get("/")
    assert response.status_code == 200