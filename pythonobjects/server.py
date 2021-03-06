import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))

    python_dictionary = {"a": 1, "b": 2}
    pickled_dictionary = pickle.dumps(python_dictionary)

    custom_product = Product("P024", "Torch", 13)
    pickled_product = pickle.dumps(custom_product)

    print("Serialized Dictionayr type: ", type(pickled_dictionary))
    print("Serialized object type: ", type(pickled_product))

    s.listen(5)
    print("Server is up. Listening for connections...")

    client, address = s.accept()
    print("Connection to ", address, "established\n")
    print("Client object ", client, "\n")

    client.send(pickled_dictionary)
    client.send(pickled_product)