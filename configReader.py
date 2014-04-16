class ConfigReader():
	def __init__(self):
		self.keys={}
	#Read Keys from file
	def readKeys(self):
		keysFile=open("config.txt","r")
		fileLines=keysFile.readlines()
		keysFile.close()
		self.keys.clear()
		for item in fileLines:
			#If last char is \n
			if (item[-1]=='\n'):
				item=item[:-1]
			#If a commented line
			if (item[0]=='#'):
				pass
			#If a new line is the first char
			elif (item[0]=='\n'):
				pass
			else:
				#Get Position of equal sign
				pos=item.index('=')
				#Name of the key is [0:pos], Value of the key is [pos+1:-1] (Stripping the \n char at the end)
				self.keys[item[0:pos]]=item[pos+1:]

	#Return the keys
	def getKeys(self):
		return self.keys
