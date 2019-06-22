from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import randint
from models.scrape import booth_scraper

app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/getrandom')
def get_random():
    response = {
        'randomNumbers': [
            {
                'randomNumber': randint(1, 100)
            },
            {
                'randomNumber': randint(1, 100)
            },
            {
                'randomNumber': randint(1, 100)
            },
        ]
    }
    return jsonify(response)


@app.route('/api/gettitle')
def get_title():
    title = booth_scraper.scrape_title('https://booth.pm/ja/items')
    response = {
        'title': title
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
