import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 4571))

    while True:
        msg = s.recv(1024)

        if not msg:
            print("No message from the server. Closing the connection...")

        product_object = pickle.loads(msg)
        
        print("Product ID: ", product_object.pid)