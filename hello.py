from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Rota principal (home) que exibe "Hello World!" e a data/hora
@app.route('/')
def home():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', time=current_time)

@app.route('/user/<name>')
def hello_name(name):
    return render_template('hello_name.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('rotainexistente.html'), 404



if __name__ == '__main__':
    app.run(debug=True)