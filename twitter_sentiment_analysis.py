# Sentiment Analysis - understanding and extracting feelings from data
# an API - allows access to apps' functionality from code
# tweepy - access Twitter API
# TextBlob - NLP tasks (perform sentiment analysis on each tweet)

# dependencies
import tweepy
from textblob import TextBlob

# 1. authenticate
consumer_key = "CONSUMER_KEY_HERE"
consumer_secret = "CONSUMER_SECRET_HERE"

access_token = "ACCESS_TOKEN_HERE"
access_token_secret = "ACCESS_TOKEN_SECRET_HERE"

# 2. authorize access to tweets
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# 3. retreive tweets
public_tweets = api.search("Carson Wentz")

# 4. tokenize
for tweet in public_tweets:
	print(tweet.text)
	# 5. perform sentiment analysis on tweets
	tweet.text
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
