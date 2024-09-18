from flask import Flask, render_template, request
import os
import analyze_image  # Dein externes Skript zur Bildanalyse

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Analyse des Bildes mit dem externen Skript
            result = analyze_image.analyze(file.stream)
            return f"Ergebnis der Analyse: {result}"
    return "Fehler beim Hochladen des Bildes."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
