import requests
import json
from langdetect import detect
import math
langs = {'en': 'eng', 'de':'ger', 'es':'spa', 'fr':'fre'}

def main():
    value = 0
    #while true:
    tweets = getTweets() #gets tweets in the form of json every 5 mins, written by madhav and ahan
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
        else:
            print "Another language"
            continue

def languageDetect(str):
    if detect(str) in langs.keys() :
        return langs[detect(str)]
    return None

def getTweets() :
    #Data comes here
    return [
    ('Need someone to shoot Donald Trump in his heart',0),
    ("It's June 11, 2016 at 04:20AM and donaldtrump is still a dangerous moron",1),
    ("Trump is already hurting us",5),
    ("This is another reason I endorse Hillary Clinton for president. Well said.",13),
    ("Hillary clinton is terribly good",10),
    ("Love her or hate her, you can't deny @HillaryClinton had a killer week.",62),
    ("I idolize Clinton", 11000)
    ]

def parseText(str) :
    return str.replace('#','',len(str))

main()
