#Source - http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from TwitterAPI import TwitterAPI
import json
import os
import sys
from credentials import credentials
import pandas as pd

#Variables that contains the user credentials to access Twitter API 
# Load credentials from ~/.credentials.json
creds = credentials.require(['access_token', 
                             'access_token_secret', 
                             'consumer_key',
                             'consumer_secret'])

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(creds.consumer_key, creds.consumer_secret)
    auth.set_access_token(creds.access_token, creds.access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #Grab Draft King data
    data_DK = pd.read_csv("../Data_Engineering_Project/data/DKSalaries_2016_06_26.csv")

    #Grab the players
    DK_names = list(data_DK["Name"])
    stream.filter(track='Jose Reyes')