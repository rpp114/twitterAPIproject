import tweepy
from twitterKeys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_key)

api = tweepy.API(auth)

search_term = raw_input("Search twitter for: ")

public_tweets = tweepy.Cursor(api.search,q=search_term,count=100).items()

for i in range(10):
    status = public_tweets.next()
    print status.text
#
# outfile = open('oneItem.txt', 'w')
#
# outfile.write(str(public_tweets.next()))
#
# outfile.close()
#
# print 'Wrote one item to file'
#
#
#

# tweet =  public_tweets[0]
# print 'Searched for: %s' % search_term
# print 'Number of tweets found: %d' % len(public_tweets)
#
# raw_input()
# counter = 1
#
# for tweet in public_tweets:
#     print 'Tweet #%d' % counter
#     counter = counter + 1
#     print 'Tweet: %s' % tweet.text
#     print 'User: %s' % tweet.author.screen_name
