from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_eye_color(parent1_color, parent2_color):
    # Genetische berekeningslogica op basis van de gegeven tabel
    # Pas dit aan volgens je eigen logica

    # Voor dit eenvoudige voorbeeld nemen we slechts één mogelijk resultaat
    possible_eye_colors = ['Groen']

    return possible_eye_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        parent1_color = request.form['parent1']
        parent2_color = request.form['parent2']

        # Bereken de oogkleur van het kind
        child_eye_colors = calculate_eye_color(parent1_color, parent2_color)

        return render_template('index.html', child_eye_colors=child_eye_colors)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
