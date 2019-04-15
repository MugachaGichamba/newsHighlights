from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://newsapi.org/v2/sources?apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    news = requests.get(url).json().get("sources")
    print(news)
    return render_template('index.html', news=news)


@app.route('/article/<string:id>')  # example.com/hello/Anthony
def article(id):
    url = 'https://newsapi.org/v2/sources?id="abc-news"&apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    print(requests.get(url).json())
    return 'Hello ' + id + '!'  # returns hello Anthony!
