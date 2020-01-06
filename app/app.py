from flask import Flask,render_template
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        
    mylist = zip(news,desc,img)
        
    return render_template('index.html', context = mylist)



@app.route('/')
def aljazeera ():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
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
        
    mylist = zip(news,desc,img)
        
    return render_template('aljazeera.html', context = mylist)


@app.route('/')
def abc ():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")
    
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        
    mylist = zip(news,desc,img)
        
    return render_template('abc.html', context = mylist)

        
        
@app.route('/')
def ansa ():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="ansa-news")
    
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        
    mylist = zip(news,desc,img)
        
    return render_template('ansa.html', context = mylist)


@app.route('/asso')
def Associatedpress():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="associated-press")
    
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        
    mylist = zip(news,desc,img)
        
    return render_template('asso.html', context = mylist)

if __name__== "__main__":
    app.run(debug=True)
