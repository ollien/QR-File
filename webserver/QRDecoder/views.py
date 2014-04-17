from django.http import HttpResponse
import base64
import zlib
import magic

def index(request):
	return HttpResponse("Woo!")

def makeData(request,base_64):
	# return HttpResponse(base_64)
	zipped=base64.b64decode(base_64)
	unzipped=zlib.decompress(zipped)
	return HttpResponse(unzipped,mimetype=magic.from_buffer(unzipped,mime=True))