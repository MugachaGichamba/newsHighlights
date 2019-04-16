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


@app.route('/article/<string:id>')
def article(id):
    # print(id)
    # # url = f'https://newsapi.org/v2/sources?id={id}&apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    # print(requests.get('https://newsapi.org/v2/sources?id=mirror&apiKey=57aa9f751dd44bb096ccd3b24857c51b').json())
    return 'Hello ' + id + '!'


@app.route('/sources')
def sources():
    url = 'https://newsapi.org/v2/sources?apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    news = requests.get(url).json().get("sources")
    print(news)
    return render_template('sources.html', news=news)

