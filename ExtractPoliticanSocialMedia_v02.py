import tweepy

CONSUMER_KEY = 'PASTEHERE'
CONSUMER_SECRET = 'PASTEHERE'
OAUTH_TOKEN = 'PASTEHERE-UXOUNFIKl0ZVRpwSECtgASty4lvmQy'
OAUTH_TOKEN_SECRET = 'PASTEHERE'

def gettweets(ID): 
          
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 
        api = tweepy.API(auth) 
        Ntweets=200
        tweets = api.user_timeline(screen_name=ID, count=Ntweets, include_rts = False) 
    
        Results = [tweet.text for tweet in tweets]
        
        print("Priting the raw data extracted:")
        print(Results)
  
if __name__ == '__main__': 
  
    print("Getting 200 tweets posts from Donald Trump twitter account: ")
    print("----------------------------------------------------------------------")
    gettweets("realDonaldTrump")  
    print("----------------------------------------------------------------------")
    print("Gettin 200 tweets posts from Joe Binden twitter account: ")
    print("----------------------------------------------------------------------")
    gettweets("JoeBiden")  
    print("----------------------------------------------------------------------")