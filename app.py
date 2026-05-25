import os

from flask import Flask, jsonify

app = Flask(__name__)

ROTAS = [
    ("/", "Página inicial (lista de rotas)"),
    ("/status", "Status do sistema"),
    ("/livros", "Lista de livros"),
    ("/autores", "Lista de autores"),
    ("/contato", "Contato"),
    ("/cadastro-livro", "Cadastro de livros"),
]


@app.route("/")
def home():
    links = "".join(
        f'<li><a href="{path}">{path}</a> — {desc}</li>'
        for path, desc in ROTAS
    )
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <title>Sistema de Gestão de Biblioteca</title>
        <style>
            body {{ font-family: system-ui, sans-serif; max-width: 640px; margin: 2rem auto; padding: 0 1rem; }}
            h1 {{ color: #1a1a2e; }}
            a {{ color: #0f3460; }}
            li {{ margin: 0.5rem 0; }}
        </style>
    </head>
    <body>
        <h1>Sistema de Gestão de Biblioteca</h1>
        <p>Clique em uma rota para ver o JSON da API:</p>
        <ul>{links}</ul>
    </body>
    </html>
    """


@app.route("/status")
def status():
    return jsonify(
        {"mensagem": "Sistema desenvolvido em Flask para estudo de CI/CD"}
    )


@app.route("/livros")
def livros():
    return jsonify({"mensagem": "Lista de livros cadastrados"})


@app.route("/autores")
def autores():
    return jsonify({"mensagem": "Lista autores cadastrados"})


@app.route("/contato")
def contato():
    return jsonify({"mensagem": "Página de contato do sistema"})


@app.route("/cadastro-livro")
def cadastro_livro():
    return jsonify({"mensagem": "Formulário de cadastro de livros"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
