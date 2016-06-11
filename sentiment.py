import requests
import json
from langdetect import detect
import math
import stream
import time
import re

langs = {'en': 'eng', 'de':'ger', 'es':'spa', 'fr':'fre'}

def main():
    print "Main method"
    value = 0
    counter = 0
    while True:
        #gets tweets in the form of json every 5 mins, written by madhav and ahan
        print "Entered while true"
        while(len(getTweets()) > 1):
            print "No. of tweets are greater than 1"
            t1 = time.time()
            t2 = t1
            tweets = getTweets()
            for tweet in tweets:
                counter+=1
                print "Entered for loop"
                likes = tweet[1] #from json
                text = parseText(tweet[0])
                print text
                if likes == 0:
                    likes = 1
                if languageDetect(text):
                    request = requests.get('https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text='+text+'&highlight_expression=links&language='+languageDetect(text)+'&apikey=94e05306-8b24-43aa-97d5-ab809eedf4e1').text
                    request_json = json.loads(request)
                    score = request_json['aggregate']['score']
                    value += score*likes
                    stream.tweets.pop(0)
                    if(counter == 1):
                        break

                else: #if the language isn't english spanish french or german
                    print "Reached else clause"
                    t2 = time.time()
                    time.sleep(10 - (t2 - t1))
            temp = value
            value = 0
            counter = 0
            print temp
            return temp

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


# main()
