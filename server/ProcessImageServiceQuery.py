from ImageDownloader import _ImageDownloader
from DirectoryManager import _DirectoryManager
from Image import _Image

class ProcessImageServiceQuery:
	def __init__(self):
		pass

	def run(self, url):
		print 'ProcessImageServiceQuery: run, url [', url, ']'

		originalFilepath = _DirectoryManager.getOriginalFilepath(url)
		processedFilepath = _DirectoryManager.getProcessedFilepath(url)

		self.process(originalFilepath, processedFilepath, url)

	def process(self, originalFilepath, processedFilepath, url):
		_ImageDownloader.download(url, originalFilepath)
		_Image.copy(originalFilepath, processedFilepath)