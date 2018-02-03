class ServerConfig:
	def __init__(self, host, port, is_debug):
		self.host = host
		self.port = port
		self.is_debug = is_debug

	def getPort(self):
		return self.port

	def getHost(self):
		return self.host

	def isDebug(self):
		return self.is_debug