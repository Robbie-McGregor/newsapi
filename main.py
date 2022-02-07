from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main():
    api_url = 'https://newsapi.org/v2/top-headlines?country=nz&apiKey=16cd803654d64cbf89e2ec14545f30ad&language=en'
    api_response = requests.get(api_url)
    news_items = api_response.json()
    return render_template('index.html', articles=news_items['articles'])

if __name__ == '__main__':
    app.run(debug=True, port=80)