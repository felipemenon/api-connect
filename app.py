from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios), 200


@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Nenhum dado foi enviado"
        }), 400

    if not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Os campos nome e email são obrigatórios"
        }), 400

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201


@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    return jsonify(usuario), 200


@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados.get("nome", usuario["nome"])
            usuario["email"] = dados.get("email", usuario["email"])

            return jsonify(usuario), 200

    return jsonify({
        "erro": "Usuário não encontrado"
    }), 404


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def remover_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return "", 204

    return jsonify({
        "erro": "Usuário não encontrado"
    }), 404


if __name__ == "__main__":
    app.run(port=5000, debug=True)