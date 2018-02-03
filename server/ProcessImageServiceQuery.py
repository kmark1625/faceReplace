from ImageDownloader import _ImageDownloader
from DirectoryManager import _DirectoryManager
from Image import _Image
import numpy as np
import cv2

class ProcessImageServiceQuery:
	def __init__(self):
		pass

	def run(self, url):
		print('ProcessImageServiceQuery: run, url [', url, ']')

		if url.startswith('data'):
			raise ValueError('Bad link')

		originalFilepath = _DirectoryManager.getOriginalFilepath(url)
		processedFilepath = _DirectoryManager.getProcessedFilepath(url)
		replacementImageFilepath = _DirectoryManager.getReplacementImageFilepath()

		_ImageDownloader.download(url, _DirectoryManager.getImageTmpFilepath(url), _DirectoryManager.getProcessedFilepath())
		_Image.copy(originalFilepath, processedFilepath)


		originalImage = cv2.imread(originalFilepath)
		replacementImage = cv2.imread(replacementImageFilepath)

		cv2.imwrite(processedFilepath, originalImage)

		originalFace = self.getLargestFace(originalImage)
		# replacementFace = self.getLargestFace(replacementImage)

		# if originalFace == None or replacementFace == None:
		# 	raise ValueError('No faces')

		# processedImage = self.replaceFace(originalImage, originalFace, replacementImage, replacementFace)

		# cv2.imwrite(processedFilepath, processedImage)


	def getLargestFace(self, image):
		faces = self.getFaces(image)
		return faces[0] if len(faces) > 0 else None

	def getFaces(self, image):
		face_cascade = cv2.CascadeClassifier('/Users/aaron/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier('/Users/aaron/opencv/data/haarcascades/haarcascade_eye.xml')
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		return face_cascade.detectMultiScale(gray, 1.3, 5)

	def replaceFace(self, originalImage, originalFace, replacementImage, replacementFace):
		x, y, w, h = originalFace
		cv2.rectangle(originalImage,(x,y),(x+w, y+h),(0,255,0),3)
		return originalImage

		# scale lebronFace
		# modify original image


