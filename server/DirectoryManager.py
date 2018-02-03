import urlparse, os

class DirectoryManager:
	def __init__(self):
		self.counter = 0
		self.ids = {}
		pass

	def getImageId(self, url):
		if not url in self.ids:
			self.ids[url] = self.counter
			self.counter += 1

		return str(self.ids[url])

	def getExtension(self, url):
		path = urlparse.urlparse(url).path
		_, extension = os.path.splitext(path)
		return extension if extension else '.jpg'

	def getOriginalFilepath(self, url):
		return 'database/' + self.getImageId(url) + '-original' + self.getExtension(url)

	def getProcessedFilepath(self, imageId):
		return 'database/' + str(imageId) + '-processed.jpg'

_DirectoryManager = DirectoryManager()