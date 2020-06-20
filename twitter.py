import tweepy as tw 
import json

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#100daysofcode -filter:retweets"
date = "2020-06-19"

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date).items()


with open("tweets", "w") as f:
    for tweet in tweets:
        json.dump(tweet._json, f)