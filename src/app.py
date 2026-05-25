from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "Sistema de Gestão de Biblioteca"}

@app.route("/status")
def status():
    return {"Sistema desenvolvido em Flask para estudo de CI/CD"}

@app.route("/livros")
def livros():
    return {"Lista de livros cadastrados"}

@app.route("/autores")
def autores():
    return {"Lista autores cadastrados"}

@app.route("/contato")
def contato():
    return {"Página de contato do sistema"}

@app.route("/cadastro-livro")
def cadastro_livro():
    return {"Formulário de cadastro de livros"}

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)