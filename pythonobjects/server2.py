import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind(("localhost",4571))

	custom_object = Product('P024', 'Torch', 13)
	pickled_object = pickle.dumps(custom_object)
	pickled_object2 = pickle.dumps(custom_object)

	s.listen(5)

	print('Server is up. Listening for connections...\n')

	client, address = s.accept()
	print('Connection to', address, 'established\n')
	print('Client object:', client, '\n')

	client.send(pickled_object2)