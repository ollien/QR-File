import base64
import zlib

def file2b64(inFile,gzip=True):
	if type(inFile)==file:
		if 'r' not in inFile.mode:
			raise IOError("File isn't open for reading")
	elif type(inFile)==str:
		path=inFile
		inFile=open(path,'r')
	else:
		raise ValueError("inFile must be a str or file object (and be open for reading) ")
	fileValue=getFileValue(inFile)
	value=''
	if gzip:
		value=zlib.compress(fileValue)
	else:
		value=fileValue
	return base64.b64encode(value)
		
def getFileValue(inFile):
	if type(inFile)==file:
		if 'r' not in inFile.mode:
			raise IOError("File isn't open for reading")
	else:
		raise ValueError("inFile must be a file object")
	value=""
	while True:
		line=inFile.read()
		if line=='':
			break
		else:
			value+=line
			
	return value
		