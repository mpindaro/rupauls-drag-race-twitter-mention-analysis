import pandas as pd
import numpy as np
import time
import twitter
import json
from twitter import TwitterHTTPError
import requests
from requests import HTTPError

def tweets_to_csv_mention_graph(filejson,filecsv):
	df_sporco = pd.read_json(filejson)
	
	for key,values in df_sporco.iterrows():
		data = values['data']
		try:
			if data['entities']['mentions']: continue
		except (KeyError,TypeError):
			df_sporco.drop(key,inplace=True)
	
	data = df_sporco['data']
	authors = [tweet['author_id'] for tweet in data]
	mentions_list = list(map(lambda x: [y['username'] for y in x],\
			[tweet['entities']['mentions'] for tweet in data]))
			
	twitter_keys = json.load(open('application_keys.json'))['twitter']
	consumer_key = twitter_keys['API_key']
	consumer_secret = twitter_keys['API_secret']
	bearer_token = twitter.oauth2_dance(consumer_key=consumer_key,consumer_secret=consumer_secret)
	twitter_api = twitter.Twitter(auth=twitter.OAuth2(bearer_token=bearer_token))
	
	count = 0
	mentioned_list = []
	for mentions in mentions_list:
		mentioned_ids=[]
		for mention in mentions:
			try:
				id_str = twitter_api.users.show(screen_name=mention)['id_str']
				mentioned_ids.append(id_str)
			except TwitterHTTPError: pass
			count+=1
			if count%898 == 0:
				print('Count: {}, sleep start'.format(count))
				time.sleep(15*60)
				print('Sleep end')
		mentioned_list.append(mentioned_ids)
		
	df_csv = pd.DataFrame()
	for author,mentions in zip(authors,mentioned_list):
		for mention in mentions:
			df_csv = df_csv.append({'source': author,\
						'target': mention,\
						'weight': 1},ignore_index=True)
						
	df_csv_weight = pd.DataFrame({'weight' : \
			df_csv.groupby( [ "source", "target"] ).size()})\
			.reset_index()
	
	df_csv_weight.to_csv(filecsv,index=False)
	
	
		
		
