# Based off code from http://geduldig.github.io/TwitterAPI/faulttolerance.html
from itertools import islice
from time import sleep

from credentials import credentials
from ftfy import fix_text
from textblob import TextBlob
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager
from TwitterAPI import TwitterRequestError
from TwitterAPI import TwitterConnectionError
import pandas as pd
from collections import defaultdict
import time
import json
import os
import sys
from credentials import credentials

#Variables that contains the user credentials to access Twitter API 
# Load credentials from ~/.credentials.json
creds = credentials.require(['access_token', 
                             'access_token_secret', 
                             'consumer_key',
                             'consumer_secret'])

api = TwitterAPI(creds.consumer_key,
                 creds.consumer_secret,
                 creds.access_token,
                 creds.access_token_secret,
                 auth_type='oAuth2')
#Grab Draft King data
data_pitchers = pd.read_csv("../Data_Engineering_Project/data/pitchers_2016_06_26.csv")
data_batters = pd.read_csv("../Data_Engineering_Project/data/batters_2016_06_26.csv")
data_DK = pd.read_csv("../Data_Engineering_Project/data/DKSalaries_2016_06_26.csv")

#Grab the players
pitchers_names = data_pitchers["Player Name"]
batters_names = data_batters["Player Name"]
DK_names = data_DK["Name"]
#Concatenate the batters and pitchers and drop dups
frames = [pitchers_names,batters_names]
all_players= pd.concat(frames)
all_players = all_players.drop_duplicates()
#Do some data cleaning so that the Data is easier to match up later
cleanplayerlst = []
for i in list(batters_names):
    test = i.split(",")
    test[0],test[1] = test[1],test[0]
    test = test[0].strip() + " " + test[1]
    cleanplayerlst.append(test)
#build list of iterators
iterator_list = [TwitterRestPager(api, 'search/tweets', {'q':name}).get_iterator(wait=2)for name in cleanplayerlst]
player_dict = defaultdict(list)
count = 0
try:
    for player, iterator in enumerate(iterator_list):
        count += 1
        print "Player Count:",count
        if player !=0 and player % 60  == 0:
            time.sleep(1200)
        for idx, item in enumerate(iterator):
            if idx == 40:
                break
            if 'text' in item:
                player_dict[cleanplayerlst[player]].append(item['text'])
            elif 'message' in item:
                raise Exception(item['message'])
        with open('twitter_batter_data.json', 'w') as fp:
            text=json.dump(player_dict, fp, indent=2)
except TwitterRequestError as e:
    if e.status_code < 500:
        raise
    else:
        # temporary interruption, re-try request
        pass
except TwitterConnectionError:
    # temporary interruption, re-try request
    pass