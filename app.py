from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    r = requests.get(url)
    print(r.json())
    return render_template('index.html')

