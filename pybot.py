#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'buNSbjqxHVXX9Jx5iokJYDrnf'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'QxDHTWyBMcvKuGsux2pPa9gzDCsspUMw3gjNK8DZbTydklTKzU'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '243822834-1y0GzpGHeIUBaTQqxOOrASaOj9c9SOu9Es9DpWeP'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Iw1nWVhjtbZUBSt4fMz30YphvZRdB2Dzhv4sBrFQmfZm8'#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)