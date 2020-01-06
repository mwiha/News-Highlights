class Config:
    '''
     General configuration parent class
    '''
    pass

NEWS_API_BASE_URL =('https://newsapi.org/v2/top-headlines?' 'country=us&' 'apiKey=c2dc80373e954e7fbd0678a357875019')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True