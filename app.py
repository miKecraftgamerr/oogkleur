from flask import Flask, request, jsonify

app = Flask(__name__)

def genetische_berekeningen(parent1, parent2, inLaw1, inLaw2):
    # Doe hier je genetische berekeningen op basis van de opgegeven tabel
    kansOpBruin = 0
    kansOpGroen = 0
    kansOpBlauw = 0

    # Voer hier je eigen genetische berekeningen uit

    return {'kansOpBruin': kansOpBruin, 'kansOpGroen': kansOpGroen, 'kansOpBlauw': kansOpBlauw}

@app.route('/calculate_eye_colors', methods=['GET'])
def calculate_eye_colors():
    parent1 = request.args.get('parent1')
    parent2 = request.args.get('parent2')
    inLaw1 = request.args.get('inLaw1')
    inLaw2 = request.args.get('inLaw2')

    result
