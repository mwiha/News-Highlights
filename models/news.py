from flask import Flask
from newsapi import NewsApiClient


app = Flask(_name_)

@app.route('/')
def Index() :
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="citizen tv")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    
