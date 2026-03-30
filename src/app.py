from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "Sistema de Gerenciamento de Biblioteca"}

@app.route("/status")
def status():
    return {"Sistema desenvolvido em Flask para estudo de CI/CD"}

@app.route("/livros")
def livros():
    return {"Lista de livros cadastrados"}

@app.route("/autores")
def autores():
    return {"Lista autores cadastrados"}

if __name__ == "__main__":
    app.run(debug=True)