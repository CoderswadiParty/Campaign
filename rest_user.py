import tweepy
import json

ckey = 'sFH28qEj9uf9zWt8Ecws9h8jS'
csecret = '0lkJlb2jBVNeahQ40EZs84W7mhjmXLWF12AGQpqDBI8yj1pffY'
atoken = '569187100-JNgzMZAa8wY8Y0JraFNQzqPuYPBmEH7BLzk3YiE4'
asecret = '0dS8L202e6HobfGhts4Vn3Z818mz5sjThYeH8M9vKJVyq'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'HillaryClinton', count = 100, include_rts = True)

for i in stuff:
	print i
	print "-----------------------------"
# 	print json_load["text"]

