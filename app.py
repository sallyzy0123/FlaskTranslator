from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/', methods=['POST', 'GET'])
def index():
    translation = None
    if request.method == 'POST':
        text = request.form ['content']
        translation = pipe(text, max_length=100)[0]['translation_text']
        return render_template('index.html', text=text, translation=translation)
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)