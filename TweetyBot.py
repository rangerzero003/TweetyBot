import tweepy

def TweetyBot():
    CONSUMER_KEY='7neJhxfFdnOWeZ3yVY4A'
    CONSUMER_SECRET='F9C64iYkrlqntxOWNsrU4KAXHW1VwLuxmDw2i20TPwo'
    ACCESS_KEY='2278229845-4v5jAxV85HiDeEEzLnRSzfyfMGNahN5HD7aYYOc'
    ACCESS_SECRET='TyP7NxvLC01ISFvJYoRJu5WMxW521vcIloNvF8OwfA10I'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    f = open('qotd.txt', 'r')
    quote = f.readline()
    author = f.readline()
    tweet = quote
    tweet += "\n-"
    tweet += author
    api.update_status(tweet)
    #print tweet


