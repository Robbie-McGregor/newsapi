import os
from flask import Flask, render_template
import requests
import datetime

apiKey = '8df9cb2d5eeb478a98b1039ea86bf393'

app = Flask(__name__)

# Main Route
@app.route('/')
def main():
    api_url = f"https://newsapi.org/v2/top-headlines?country=nz&apiKey={apiKey}&language=en"
    news_items = apiCall(api_url)
    year = getYear()
    if news_items['status'] == "error":
        return render_template("error.html", message=news_items['message'], year=year)
    return render_template('index.html', articles=news_items['articles'], year=year)

# Route to display articles for specific category
@app.route('/articles/<category>')
def articles(category):
    api_url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={apiKey}&language=en&country=nz"
    news_items = apiCall(api_url)
    year = getYear()
    if news_items['status'] == "error":
        return render_template("error.html", message=news_items['message'], year=year)
    return render_template('index.html', articles=news_items['articles'], year=year)


# Make API call and return as JSON
def apiCall(url):
    response = requests.get(url)
    return response.json()

# Get Current Year
def getYear():
    return datetime.datetime.now().date().strftime("%Y")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)