import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 4571))
    
    while True:
        msg = s.recv(1024)

        if not msg:
            print("No meesage from server. Closing the connection...")
            break

        # print("Message from serer: ", msg.decode("utf-8"))
        print("Type of recieved message:", type(msg))
        print("Message_data: ", msg)

        unpickled_message = pickle.loads(msg)

        print("Type of deserialized message: ", type(unpickled_message))
        print("Desiliarized message: ", unpickled_message)