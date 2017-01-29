import tweepy
from textblob import TextBlob
import json

consumer_key = "G6Otvf4vudduGS2tv7PIrIJXh"
consumer_secret = "LDRFwYSJdLr3kwbuYwNtaUfe2Q7CE9n3KgqMhuOSz3JA97WmgB"
access_token = "823193458177409024-tVaTHYhbUEi20y1nHLlKJLc7EBS2DiT"
access_token_secret = "gxyir3XQsNQk3lgjWdLiGlJVHPCJYdvDQjsd5W2gcfyn9"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets_not_subjective = []
tweets_subjective = []
tweets_positive = []

tweets_public = api.search("soda")
for i in range(0,2):
	for tweets in tweets_public :
		#print(tweets.text)
		#print(tweets.created_at)
		sent = TextBlob(tweets.text)
        if sent.sentiment.subjectivity > 0.5:
            tweets_not_subjective.append(tweets)
        elif sent.sentiment.subjectivity < 0.5:
            tweets_subjective.append(tweets)

print tweets_subjective
print tweets_not_subjective