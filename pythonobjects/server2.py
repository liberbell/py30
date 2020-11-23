import socket
from product import Product
import pickle
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind(("localhost",4571))

	custom_object = [Product('P024', 'Torch', 13),
	                 Product('P025', 'Waterbottle', 5),
					 Product('P026', 'Keyboard', 20),
					 Product('P027', 'Mouse', 15),
					 Product('P028', 'USBcable', 2)]


	# pickled_object = pickle.dumps(custom_object)
	# pickled_object2 = pickle.dumps(custom_object)

	s.listen(5)

	print('Server is up. Listening for connections...\n')

	client, address = s.accept()
	print('Connection to', address, 'established\n')
	print('Client object:', client, '\n')

	for product in custom_object:
		pickle_product = pickle.dumps(product)
		client.send(pickle_product)

		print("Sent product: ", product.pid)

		time.sleep("")

	# s.close()