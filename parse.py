import json
import ast
import requests
with open('hillary_tweets.txt', 'r') as myfile:
   data=myfile.read().replace('\n', '')


retrieved_strings = ['{'+x+'}' for x in data.strip('{}').split('}{')]

count = 0

concept_string = ""

for el in retrieved_strings:
	content = json.loads(el)

	if "16" == content["created_at"][-2:]:
		# print content["text"]

		concept_string += content["text"]+" "

		count += 1

print concept_string

final_json = {}
index = 0

for i in range(500, len(concept_string), 1000):

	print "------"
	print concept_string[index:i]

	try:
		request = requests.get("https://api.havenondemand.com/1/api/sync/extractconcepts/v1?text="+concept_string[index:i]+"&highlight_expression=links&apikey=529a2f2f-2e03-4690-a5f7-abbfa52ae0c6").text
	except:
		continue
	index = i
	print i

	request_json = json.loads(request)
	if 'reason' not in request_json:
		print request_json
		print "Entered for"

		terms = request_json['concepts']

		for term in terms:
			key = term['concept']
		
			if key in final_json:
				final_json[key] += term['occurrences']
			else:
				# print "THIS RAN: "+str(request_json['concepts'][0]['concept'])
				final_json[key] = term['occurrences']

		# print "-------------------------------------"
		# print final_json
		# print "-------------------------------------"


print final_json

# request = requests.get("https://api.havenondemand.com/1/api/sync/extractconcepts/v1?text="+concept_string[5000:5500]+"&highlight_expression=links&apikey=529a2f2f-2e03-4690-a5f7-abbfa52ae0c6").text
# print request
