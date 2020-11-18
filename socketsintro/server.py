import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',4571))
s.listen(5)

print("Server is up. Listening for connections....")