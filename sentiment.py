import requests
import json
from langdetect import detect
import math
import stream
import time
import re

langs = {'en': 'eng', 'de':'ger', 'es':'spa', 'fr':'fre'}

def main():
    value = 0
    while True:
        #gets tweets in the form of json every 5 mins, written by madhav and ahan
        #
        while(len(getTweets()) > 1):
            tweets = getTweets()
            for tweet in tweets:
                likes = tweet[1] #from json
                text = parseText(tweet[0])
                if likes == 0:
                    likes = 1
                if languageDetect(text):
                    request = requests.get('https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text='+text+'&highlight_expression=links&language='+languageDetect(text)+'&apikey=94e05306-8b24-43aa-97d5-ab809eedf4e1').text
                    request_json = json.loads(request)
                    score = request_json['aggregate']['score']
                    value += score*likes
                    print text, value/10.0
                    value=0
                    stream.tweets.pop(0)
                else:
                    print "Another language"
                    continue
        #time.sleep(4.5)

def languageDetect(str):
    if detect(str) in langs.keys() :
        return langs[detect(str)]
    return None

def getTweets() :
    return stream.getTweets()

def parseText(str) :
    temp = str
    for i in str:
        if not(i.isalpha() or i.isspace()):
            str = str.replace(i, '', len(temp))
    return str


main()
