from flask import Flask, request, jsonify

app = Flask(__name__)

CATEGORIAS = [
    "Pedagógico",
    "Financeiro",
    "Documentos",
    "Matrícula",
    "Justificativa de Ausência",
    "Outros"
]

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "projeto": "Classificador Inteligente de Mensagens",
        "categorias": CATEGORIAS
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)