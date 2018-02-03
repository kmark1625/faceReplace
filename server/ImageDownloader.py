import urllib.request

class ImageDownloader:
	def __init__(self):
		pass

	def download(self, url, destination):
		print('ImageDownloader: downloadImage, url [', url, '], destination [', destination, ']')
		urllib.request.urlretrieve(url, destination)

_ImageDownloader = ImageDownloader()