from flask import Flask, request, jsonify, render_template
from sequence_utils import analyze_sequence
from diseases_mapping import disease_variant_map

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get('sequence', '').upper()

    if not sequence:
        return jsonify({"error": "No DNA sequence provided"}), 400

    analysis = analyze_sequence(sequence)

    potential_diseases = []
    for variant, detected in analysis.items():
        if detected and variant in disease_variant_map:
            variant_info = disease_variant_map[variant]
            potential_diseases.append({
                "variant_type": variant,
                "diseases": variant_info
            })

    return jsonify({
        "sequence_analysis": analysis,
        "potential_diseases": potential_diseases
    })

if __name__ == '__main__':
    app.run(debug=True, port=5020)