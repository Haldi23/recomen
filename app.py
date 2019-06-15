from flask import Flask, render_template
from models.scrape import booth_scraper

app = Flask(__name__)


@app.route('/')
def index():
    title = 'れこめん'
    message = 'レモンだ？貴様この野郎'
    return render_template('index.html', title=title, message=message)


@app.route('/test')
def test():
    title = 'れこめん'
    itemdatas = booth_scraper.boothscrape('https://booth.pm/ja/items')
    message = itemdatas
    return render_template('index.html', title=title, message=message)


if __name__ == "__main__":
    app.run(debug=True)
