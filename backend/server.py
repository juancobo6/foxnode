from flask import Flask, request, jsonify
from flask_cors import CORS

from foxnode import foxnode

app = Flask(__name__)
CORS(app)

@app.route('/generate_diagram', methods=['POST'])
def generate_diagram():
    data = request.get_json()
    prompt = data['prompt']
    diagram_mermaid = foxnode(prompt)
    return jsonify({'diagram': diagram_mermaid})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3001)