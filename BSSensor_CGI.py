import tweepy
from textblob import TextBlob
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

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
tweets_negative = []
sentiment_array = []
subjectivity_array = []
count1 = 0
count2 = 0
search_term = HOMO

tweets_public = api.search(search_term)
for tweets in tweets_public:
    #print(tweets.text)
    #print(tweets.created_at)
    sent = TextBlob(tweets.text)
    #print(sent.sentiment)
    sentiment_array.append(sent.sentiment.polarity)
    subjectivity_array.append(sent.sentiment.subjectivity)
    if sent.sentiment.subjectivity < 0.5:
        tweets_not_subjective.append(tweets)
    elif sent.sentiment.subjectivity > 0.5:
        tweets_subjective.append(tweets)
        if sent.sentiment.polarity > 0.0:
            tweets_positive.append(tweets)
        elif sent.sentiment.polarity < 0.0:
            tweets_negative.append(tweets)
            count1 += sent.sentiment.subjectivity
            count2 += sent.sentiment.polarity
            average1 = count1/15
            average2 = count2/15
#for k in tweets_positive:
#	sev = TextBlob(k.text)
#	print(sev.sentiment)

trace0 = go.Scatter(
    x = sentiment_array,
    y = subjectivity_array,
    mode = 'markers',
    name = 'markers'
)

#trace1 = go.Scatter(
 #   k = [0],
  #  f = [0.3]
#)
#data = [trace0]

# Plot and embed in ipython notebook!
py.plot(data, filename='line-mode')
#py.plot(data, filename='basic-line')

