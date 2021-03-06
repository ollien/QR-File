from django.http import HttpResponse
import base64
import zlib
import magic
import json
from operator import itemgetter
def index(request):
	return HttpResponse("Woo!")

def makeData(request,file_id,part_id,base_64):
	# return HttpResponse(base_64)
	#zipped=base64.b64decode(base_64)
	#unzipped=zlib.decompress(zipped)
	if (base_64[-1]!='_'):
		cookies=request.COOKIES
		parts=""
		parsedCookies=[]
		for cookieName in cookies.keys():
			cookie=cookies[cookieName]
			print cookieName
			fail=False
			parsedCookie=None
			try:
				parsedCookie=json.loads(cookie)
			except:
				fail=True
				print 'failed'
			print '--'
			# print parsedCookie
			if not fail:
				parsedCookies.append(parsedCookie)
		for item in parsedCookies:
			item['partId']=int(item['partId'])
		#Removing duplicates
		partIds=list(set(map(itemgetter('partId'),parsedCookies)))
		tempList=[]
		for item in parsedCookies:
			if item['partId'] in partIds:
				del partIds[partIds.index(item['partId'])]
				tempList.append(parsedCookies[parsedCookies.index(item)])
				
		#Done removing duplicates
		parsedCookies=sorted(tempList,key=itemgetter('partId'))
		for item in parsedCookies:
			print item['partId']
		
		for cookie in parsedCookies:
				part=cookie['part']
				if part[-1]=='_':
					parts+=part[:-1]
				else:
					parts+=part
				print 'added '+part
		parts+=base_64
		print '--'
		print parts
		zipped=base64.b64decode(parts)
		unzipped=zlib.decompress(zipped)
		return HttpResponse(unzipped,mimetype=magic.from_buffer(unzipped,mime=True))
					
		#return HttpResponse(unzipped,mimetype=magic.from_buffer(unzipped,mime=True))
	else:
		print type(json.dumps({
	'fileId':file_id,
	'partId':part_id,
	'part':base_64
}))
		response=HttpResponse("Part added, add other parts")
		response.set_cookie(file_id+'_'+part_id,json.dumps({
			'fileId':file_id,
			'partId':part_id,
			'part':base_64
		}),path='/decode')
		return response
