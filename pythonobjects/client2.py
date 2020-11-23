import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(("localhost", 4571))

	while True:
		msg = s.recv(1024)

		if not msg:
			print('No messages from the server. Closing the connection...')
			break

		# print('Type of received message:', type(msg))
		# print('Message data:', msg)

		# unpickled_msg = pickle.loads(msg)
        procuct_object = pickle.loads(msg)

		# print('Type of deserialized message:', type(unpickled_msg))
		# print('Deserialized data:', unpickled_msg)

        print("Product ID: ", procuct_object.pid)