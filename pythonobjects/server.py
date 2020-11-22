import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))

    python_dictionary = {"a": 1, "b": 2}
    custom_product = Product("P024", "Torch", 13)

    s.listen(5)
    print("Server is up. Listening for connections...")

    client, address = s.accept()
    print("Connection to ", address, "established\n")
    print("Client object ", client, "\n")

    client.send(python_dictionary)
    client.send(custom_product)