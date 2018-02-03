from ImageDownloader import _ImageDownloader
from DirectoryManager import _DirectoryManager
from Image import _Image

class ProcessImageServiceQuery:
	def __init__(self):
		pass

	def run(self, url):
		print 'ProcessImageServiceQuery: run, url [', url, ']'

		originalFilepath = _DirectoryManager.getOriginalFilepath(url)
		imageId = _DirectoryManager.getImageId(url)
		processedFilepath = _DirectoryManager.getProcessedFilepath(imageId)

		_ImageDownloader.download(url, originalFilepath)
		self.process(originalFilepath, processedFilepath, imageId)

		return imageId

	def process(self, originalFilepath, processedFilepath, imageId):
		_Image.copy(originalFilepath, processedFilepath)