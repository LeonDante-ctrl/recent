from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b2a3ef2c39444fb799e98debbcdd4257")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


articles = topheadlines['articles']

desc = []
news = []
img = []

for i in range(len(articles)):
    myarticles = articles[i]

    news.append(myarticles['title'])
    desc.append(myarticles['description'])
    img.append(myarticles['urlToImage'])
