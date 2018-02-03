import os
import urllib

from flask import Flask, request, jsonify, send_file
from GetImageServiceQuery import GetImageServiceQuery
from ProcessImageServiceQuery import ProcessImageServiceQuery

class Server:
	def __init__(self, serverConfig):
		self.serverConfig = serverConfig

		self.getImageServiceQuery = GetImageServiceQuery()
		self.processImageServiceQuery = ProcessImageServiceQuery()

		self.app = Flask(__name__)
		self.app.add_url_rule('/process', 'process', self.onProcessImage, methods=['GET'])
		self.app.add_url_rule('/images/<int:imageId>', 'images', self.onGetImage, methods=['GET'])

	def startServer(self):
		self.app.run(host=self.serverConfig.getHost(), port=self.serverConfig.getPort(), debug=self.serverConfig.isDebug())

	def onProcessImage(self):
		encodedUrl = request.args['url']
		url = Server.parseUrl(encodedUrl)
		print 'Server: onProcessImage, encodedurl [', encodedUrl, '], url [', url, ']'

		imageId = self.processImageServiceQuery.run(url)

		return jsonify({
			'imageId': imageId,
			'url' : self.getUrlForImageId(imageId)
		})

	def onGetImage(self, imageId):
		print 'Server: onGetImage, imageId [', imageId, ']'
		
		filepath = self.getImageServiceQuery.run(imageId)
		
		return send_file(filepath, mimetype='image/jpg')

	@staticmethod
	def parseUrl(encodedUrl):
		return urllib.unquote(encodedUrl).decode('utf8')

	@staticmethod
	def parseUrlFromRequest(request):
		requestBody = request.get_json(force=True)
		return requestBody['url']

	def getUrlForImageId(self, imageId):
		return 'http://localhost:3000/images/' + str(imageId)

# http%3A%2F%2Fa.espncdn.com%2Fcombiner%2Fi%3Fimg%3D%2Fi%2Fheadshots%2Fnba%2Fplayers%2Ffull%2F1966.png%26w%3D350%26h%3D254
# https%3A%2F%2Fmk0slamonlinensgt39k.kinstacdn.com%2Fwp-content%2Fuploads%2F2018%2F02%2Flebon_warriors_response.jpg