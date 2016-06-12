import json
import ast
import requests
from datetime import datetime

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='AhanM', api_key='2117axpgdr')
import numpy as np
from langdetect import detect
import time


with open('trump_tweets.txt', 'r') as myfile:
	 data=myfile.read().replace('\n', '')


retrieved_strings = ['{'+x+'}' for x in data.strip('{}').split('}{')]

json_objs = []

for obj in retrieved_strings:
	dictionary = json.loads(obj)
	if "2016" in dictionary['created_at']:
		json_objs.append(json.loads(obj))

def swap( A, x, y ):
	tmp = A[x]
	tmp2 = json_objs[x]
	A[x] = A[y]
	json_objs[x] = json_objs[y]
	A[y] = tmp
	json_objs[y] = tmp2


def extract_datetime(x):

	return datetime.strptime(x['created_at'][:20]+x['created_at'][-4:],'%a %b %d %H:%M:%S %Y')

def sort():

	# extract datetime objcets from created_at
	# datetime.striptimie()
	global json_objs

	# dates = [datetime.strptime(obj['created_at'][:20]+obj['created_at'][-4:],'%a %b %d %H:%M:%S %Y') for obj in json_objs[:500]]
	# dates = [obj['created_at'] for obj in json_objs]

	# sorted_dates = sorted(dates, cmp=None, key=lambda x: parse(x, fuzzy=true), reverse=False)
	# print sorted_dates

	# for i in range( len( json_objs ) ):
	# 	least = i
	# 	for k in range( i + 1 , len( json_objs ) ):
	# 		if datetime.strptime(json_objs[k]['created_at'][:20]+json_objs[k]['created_at'][-4:], '%a %b %d %H:%M:%S %Y') < datetime.strptime(json_objs[least]['created_at'][:20]+json_objs[least]['created_at'][-4:], '%a %b %d %H:%M:%S %Y'):
	# 			least = k
 # 		swap( json_objs , least, i )

	# for i in range(len(dates)):
	# 	least = i
	# 	for k in range( i + 1 , len( dates ) ):
 # 			if dates[k] < dates[least]:
 # 				least = k
 # 		swap(dates, least, i)

	sorted_objs = []
	sorted_objs = sorted(json_objs, cmp=None, key=extract_datetime, reverse=False)

	# print dates
	return sorted_objs

# for el in retrieved_strings:
	# content = json.loads(el)
	# json_objs.append(ast.literal_eval(el))
	

sorted_objs = sort() # []

texts = [obj['text'] for obj in sorted_objs]

likes = []
for obj in sorted_objs:
	if "favourites_count" in obj:
		likes.append(obj["favourites_count"])
	else:
		likes.append(0)

dates = [datetime.strptime(obj['created_at'][:20]+obj['created_at'][-4:],'%a %b %d %H:%M:%S %Y') for obj in json_objs]

points = []
langs = {'en': 'eng', 'de':'ger', 'es':'spa', 'fr':'fre'}

def languageDetect(str):
		if detect(str) in langs.keys() :
				return langs[detect(str)]
		return None

def parseText(str) :
		temp = str
		for i in str:
				if not(i.isalpha() or i.isspace()):
						str = str.replace(i, '', len(temp))
		return str





#--------------------

pointsFile = open('points.txt', 'r')
for i in range(0,799):
	print i
	points.append(float(pointsFile.readline()))




data = [
				 go.Scatter(x=dates,y=points)
			 ]
pointsFile.close()

py.plot(data)
# main()

