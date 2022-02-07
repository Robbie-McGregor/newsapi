import os
from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def main():
    api_url = 'https://newsapi.org/v2/top-headlines?country=nz&apiKey=16cd803654d64cbf89e2ec14545f30ad&language=en'
    api_response = requests.get(api_url)
    news_items = api_response.json()
    year = datetime.datetime.now().date().strftime("%Y")
    return render_template('index.html', articles=news_items['articles'], year=year)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)