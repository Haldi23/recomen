from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import randint
from models.scrape import booth_scraper

app = Flask(__name__,
            static_folder="./frontend/dist/static",
            template_folder="./frontend/dist")
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/getrandom')
def get_random():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
