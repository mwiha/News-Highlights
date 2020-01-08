from newsapi import NewsApiClient
from flask import render_template,request,redirect,url_for
from . import main



@main.route('/')
def Index():
#     newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
#     topheadlines = newsapi.get_top_headlines(sources="")
    
#     articles = topheadlines['articles']
    
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         myarticles = articles[i]
        
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
        
#     mylist = zip(news,desc,img)
        
    return render_template('index.html')



@main.route('/aljazeera')
def Aljazeera():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    pubAt=[]

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        
    mylist = zip(news,desc,img,pubAt)
        
    return render_template('aljazeera.html', context = mylist)


@main.route('/abc')
def abc ():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")
    
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        
    mylist = zip(news,desc,img, pubAt)
        
    return render_template('abc.html', context = mylist)

        
        
@main.route('/cnn')
def Cnn():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="cnn")
    
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    pubAt = []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        
    mylist = zip(news,desc,img,pubAt)
        
    return render_template('cnn.html', context = mylist)

@main.route('/asso')
def Associatedpress():
    newsapi = NewsApiClient(api_key="c2dc80373e954e7fbd0678a357875019")
    topheadlines = newsapi.get_top_headlines(sources="associated-press")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    pubAt= []

    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        
    mylist = zip(news,desc,img,pubAt)
        
    return render_template('associatedpress.html', context = mylist)