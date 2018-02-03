import os, urllib.parse

class DirectoryManager:
	def __init__(self):
		pass

	def getImageTmpFilepath(self, decodedUrl):
		return 'database/' + str(urllib.parse.quote_plus(decodedUrl))

	def getOriginalFilepath(self, decodedUrl):
		return 'database/' + str(urllib.parse.quote_plus(decodedUrl)) + '-original.jpg'

	def getProcessedFilepath(self, decodedUrl):
		return 'database/' + str(urllib.parse.quote_plus(decodedUrl)) + '-processed.jpg'

	def getReplacementImageFilepath(self):
		return 'database/lebron.jpg'
		
_DirectoryManager = DirectoryManager()