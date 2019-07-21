# Sentiment Analysis - understanding and extracting feelings from data
# an API - allows access to apps' functionality from code
# tweepy - access Twitter API
# TextBlob - NLP tasks (perform sentiment analysis on each tweet)

# dependencies
import tweepy
from textblob import TextBlob

# 1. authenticate
consumer_key = "YcAwnVsMNOk6CKall99dMXdum" # "CONSUMER_KEY_HERE"
consumer_secret = "szIPbyqncBSAzg6jph6GfV5mglHzS2KCv6N1GLXXG0Xy9kEaIx" # "CONSUMER_SECRET_HERE"

access_token = "214328171-lr3MVoyKouWtiwaGRPzAMpiqRC3oJfWsqGUzslNl" # "ACCESS_TOKEN_HERE"
access_token_secret = "RNMBokJrtUkoH1pWo2MRmSP4w6w5b6DULMLd3W4YJacqq" # "ACCESS_TOKEN_SECRET_HERE"

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