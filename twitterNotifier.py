import tweepy
import credentials
import random

ACCESS_KEY = credentials.ACCESS_TOKEN
ACCESS_SECRET = credentials.ACCESS_TOKEN_SECRET
CONSUMER_KEY = credentials.API_KEY
CONSUMER_SECRET = credentials.API_KEY_SECRET
BEARER_TOKEN = credentials.BEARER_TOKEN


def authenticateOld():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(
        ACCESS_KEY,
        ACCESS_SECRET,
    )
    # Create API object using the old twitter APIv1.1
    api = tweepy.API(auth)
    return api

def authenticateNew():
    # This is the syntax for twitter API 2.0
    newapi = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
    )
    return newapi

def postTweet(message):
    newapi = authenticateNew()
    message = "@trungnguyen276 " + message + " - " + str(random.randint(1000, 9999)) # To avoid duplicate tweets
    post_result = newapi.create_tweet(text=message)
    print(post_result)


if __name__ == "__main__":
    postTweet("Test twitter API 2.0")
