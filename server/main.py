from Server import Server
from ServerConfig import ServerConfig

serverConfig = ServerConfig('0.0.0.0', 3000, True)
server = Server(serverConfig)
server.startServer()
