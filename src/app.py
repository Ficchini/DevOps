from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "Sistema de Gerenciamento de Biblioteca"}

@app.route("/status")
def status():
    return {"status": "Sistema desenvolvido em Flask para estudo de CI/CD"}

if __name__ == "__main__":
    app.run(debug=True)