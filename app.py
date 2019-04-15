from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    news = requests.get(url).json().get("articles")

    return render_template('index.html', news=news)

