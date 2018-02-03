from DirectoryManager import _DirectoryManager

class GetImageServiceQuery:
	def __init__(self):
		pass

	def run(self, imageId):
		return _DirectoryManager.getProcessedFilepath(imageId)