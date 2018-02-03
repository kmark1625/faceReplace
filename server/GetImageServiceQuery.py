from DirectoryManager import _DirectoryManager

class GetImageServiceQuery:
	def __init__(self):
		pass

	def run(self, decodedUrl):
		return _DirectoryManager.getProcessedFilepath(decodedUrl)