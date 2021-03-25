from credentials import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, ACCOUNT_ID, ACCOUNT_NAME
import tweepy 
from tweepy import Stream 
from tweepy.streaming import StreamListener
import json 


class StdOutListener(StreamListener): 
    def on_data(self, data): 
        clean_data = json.loads(data)
        tweetId = clean_data["id"]
        tweet = "Ta gueule LESS GOOOOOO 🔥🔥🔥 https://twitter.com/extendo64_/status/1374910500606251008/video/1"
        respondToTweet(tweet, tweetId)

def respondToTweet(tweet, tweetId): 
    api, auth = setUpAuth()

    api.update_status(tweet, in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)

def setUpAuth():
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET) 
    # authentication of access token and secret 
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
    api = tweepy.API(auth) 
    return api, auth



def followStream():
    api, auth = setUpAuth()
    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=["BotDababy"]) #filter=[ACCOUNT_ID]
    # publishTweet(tweet)



if __name__ == "__main__":
    followStream()

