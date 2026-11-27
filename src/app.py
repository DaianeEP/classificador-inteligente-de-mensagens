from flask import Flask, jsonify, request
from llm import classificar_mensagem


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "projeto": "Classificador Inteligente de Mensagens"
    })


@app.route("/classificar", methods=["POST"])
def classificar():

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "erro": "JSON não enviado."
        }), 400

    texto = dados.get("texto", "").strip()

    if not texto:
        return jsonify({
            "erro": "Informe uma mensagem para classificação."
        }), 400

    try:

        categoria = classificar_mensagem(texto)

        return jsonify({
            "mensagem": texto,
            "categoria": categoria
        })

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400

    except RuntimeError as erro:

        return jsonify({
            "erro": str(erro)
        }), 503

    except Exception:

        return jsonify({
            "erro": "Erro interno inesperado."
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )