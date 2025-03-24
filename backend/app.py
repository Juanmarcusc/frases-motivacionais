from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo à API de Frases Motivacionais! Use a rota /frase com método POST para obter frases."

# Carregar frases do arquivo JSON
with open('frases.json', 'r', encoding='utf-8') as file:
    frases = json.load(file)

@app.route('/frase', methods=['POST'])
def get_frase():
    data = request.get_json()
    emocao = data.get('emocao', 'neutro').lower()

    if emocao in frases:
        frase = frases[emocao]
        return jsonify({"frase": frase}), 200
    else:
        return jsonify({"error": "Emoção não encontrada"}), 400

if __name__ == '__main__':
    app.run(debug=True)