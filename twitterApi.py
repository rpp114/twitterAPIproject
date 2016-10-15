import tweepy
from twitterKeys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_key)

api = tweepy.API(auth)

search_term = raw_input("Search twitter for: ")

public_tweets = api.search(q=search_term,count=100)

# print public_tweets

# tweet =  public_tweets[0]
print 'Searched for: %s' % search_term
print 'Number of tweets found: %d' % len(public_tweets)

raw_input()
counter = 1

for tweet in public_tweets:
    print 'Tweet #%d' % counter
    counter = counter + 1
    print 'Tweet: %s' % tweet.text
    print 'User: %s' % tweet.author.screen_name
