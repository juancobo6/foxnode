from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_diagram', methods=['POST'])
def generate_diagram():
    data = request.get_json()
    # print("Data recivida: ", data)
    prompt = data['prompt']
    # print("Prompt recivido: ", prompt)
    diagram_mermaid = f"""graph LR
      A --- B
      B-->C[fa:fa-ban {prompt}]
      B-->D(fa:fa-spinner)"""
    return jsonify({'diagram': diagram_mermaid})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3001)