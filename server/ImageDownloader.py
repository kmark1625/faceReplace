import urllib.request
from PIL import Image

class ImageDownloader:
	def __init__(self):
		pass

	def download(self, url, destination):
		print('ImageDownloader: downloadImage, url [', url, '], destination [', destination, ']')
		urllib.request.urlretrieve(url, destination)
		self.saveAsJpeg(destination)

	def saveAsJpeg(self, destination):
		img = Image.open(destination)
		img.convert('RGB').save(destination, 'JPEG')

_ImageDownloader = ImageDownloader()