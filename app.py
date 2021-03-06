from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def sources():
    url = 'https://newsapi.org/v2/sources?apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    news = requests.get(url).json().get("sources")
    print(news)
    return render_template('sources.html', news=news)


@app.route('/sources/<id>')
def articles(id):
    url = f'https://newsapi.org/v2/top-headlines?sources={id}&apiKey=57aa9f751dd44bb096ccd3b24857c51b'
    articles = requests.get(url).json().get("articles")
    print(articles)
    return render_template('article.html', articles=articles)

