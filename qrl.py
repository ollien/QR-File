import qrcode
import re
import configReader
def checkFullURL(string):
	result=re.match('http://(www.)?\w.+/+\w*._',string) #This is regex to check for a url that begins with http://, possibly has www., and ends with /(something)_. Remove /+\w*._ to not check the ending.
	if result:
		return string
	else:
		result=re.match('http://.*',string)
		if result:
			raise ValueError("Not a valid URL.")
		else:
			result=re.match('http://*.','http://'+string)
			if result:
				return 'http://'+string
			else:
				raise ValueError("Not a valid URL.")
	
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
	try:
		baseUrl=keys['baseUrl']
	except KeyError:
		raise ValueError("No BaseURL found in config")
	max_length-=len(baseUrl)
	try:
		checkBaseURL(baseUrl)
	except ValueError:
		raise ValueError("Not a valid BaseURL")
		
	if length%4 is not 0:
		return 'not valid b64'
	