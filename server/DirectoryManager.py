import urlparse, os, urllib

class DirectoryManager:
	def __init__(self):
		pass

	def getExtension(self, url):
		path = urlparse.urlparse(url).path
		_, extension = os.path.splitext(path)
		return extension if extension else '.jpg'

	def getOriginalFilepath(self, decodedUrl):
		return 'database/' + str(urllib.quote_plus(decodedUrl)) + '-original.jpg'

	def getProcessedFilepath(self, decodedUrl):
		return 'database/' + str(urllib.quote_plus(decodedUrl)) + '-processed.jpg'

_DirectoryManager = DirectoryManager()