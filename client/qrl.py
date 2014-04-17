import qrcode
import re
import configReader
from math import ceil
def checkBaseURL(string):
	result=re.match('http://(www.)?\w.+/',string) #This is regex to check for a url that begins with http://, possibly has www., and ends with /
	if result:
		return string
	else:
		result=re.match('http://.*',string)
		if result:
			raise ValueError("Not a valid URL.")
		else:
			result=re.match('http://(www.)?\w.+/+\w*._','http://'+string)
			if result:
				return 'http://'+string
			else:
				raise ValueError("Not a valid URL.")


	
def createQR(data):
	length=len(data)
	max_length=2133 #This is the highest number I was able to get to generate a url in testing
	reader=configReader.ConfigReader()
	reader.readKeys()
	keys=reader.getKeys()
	baseUrl=None
	try:
		baseUrl=keys['baseUrl']
	except KeyError:
		raise ValueError("No BaseURL found in config")
	qrs=[]
	max_length-=len(baseUrl)
	try:
		checkBaseURL(baseUrl)
	except ValueError:
		raise ValueError("Not a valid BaseURL")
		
	if length%4 is not 0:
		return 'not valid b64'
	#Start splitting up the data into different urls
	# if len(data)<max_length:
	# 	url=baseUrl+data
	# else:
	quantity=ceil(float(len(data))/max_length)
	quantity=int(quantity)
	split=ceil(float(len(data))/quantity)
	split=int(split)
	print split
	print len(data)
	alreadySplit=0
	for i in range(quantity):
		url=baseUrl
		if alreadySplit+split<len(data):
			url+=data[alreadySplit:alreadySplit+split]
			if quantity>1:
				url+='_'
			alreadySplit+=split
		else:
			url+=data[alreadySplit:]
		qrs.append(qrcode.make(url))
	return qrs
	
	