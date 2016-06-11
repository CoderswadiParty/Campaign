#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import ast
import time
import json

from httplib import IncompleteRead
# import pandas as pd
# import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API
access_token = "569187100-JNgzMZAa8wY8Y0JraFNQzqPuYPBmEH7BLzk3YiE4"
access_token_secret = "0dS8L202e6HobfGhts4Vn3Z818mz5sjThYeH8M9vKJVyq"
consumer_key = "sFH28qEj9uf9zWt8Ecws9h8jS"
consumer_secret = "0lkJlb2jBVNeahQ40EZs84W7mhjmXLWF12AGQpqDBI8yj1pffY"

tweets = []

t1 = time.time()
t2 = t1
t3 = t1

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		t2 = time.time()
		# print t2 - t1
		if t2 - t1 < 5:

			json_load = json.loads(data)
			# if json_load["text"][:2] != "RT" and json_load["retweeted"] == False:
			# 	print json_dict["text"]
			# 	print "---------"
			if json_load["truncated"] == False and not json_load['retweeted'] and 'RT ' not in json_load['text']:
				texts = json_load['text']
				coded = texts.encode('utf-8')
				s = str(coded)

				tweets.append((s, json_load["favorite_count"]))

				# print tweets[-1]
				# print "------"

			return True

			# if json_load["text"][:2] != "RT" and json_load["retweeted"] == False:


		return False

	def on_error(self, status):
		print status

def execute():
	stream.filter(track=['Hillary','Clinton', 'Clintons', 'hillaryclinton', 'imwithher','neverhillary','sheswithus'], languages=["en"])

def main():

	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	# global t1,t2,t3
	# while (t1 - t3) < 300:
	# 	t1 = time.time()

	stream.filter(track=['Hillary','Clinton', 'Clintons', 'hillaryclinton', 'imwithher','neverhillary','sheswithus'], languages=["en"])

	#print len(tweets)
	#for i in tweets:
		#print i
if __name__ == '__main__':
	main()

def getTweets():
	main()
	return tweets
