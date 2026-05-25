import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_home():
    client = app.test_client()
    assert client is not None
    response = client.get("/")
    assert response.status_code == 200
    
def test_status():
    client = app.test_client()
    assert client is not None
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {
        "mensagem": "Sistema desenvolvido em Flask para estudo de CI/CD"
    }
    
def test_livros():
    client = app.test_client()
    assert client is not None
    response = client.get("/livros")
    assert response.status_code == 200
    
def test_autores():
    client = app.test_client()
    assert client is not None
    response = client.get("/autores")
    assert response.status_code == 200
    
def test_contato():
    client = app.test_client()
    assert client is not None
    response = client.get("/contato")
    assert response.status_code == 200
    
def test_cadastro_livro():
    client = app.test_client()
    assert client is not None
    response = client.get("/cadastro-livro")
    assert response.status_code == 200
    assert response.json == {"mensagem": "Formulário de cadastro de livros"}