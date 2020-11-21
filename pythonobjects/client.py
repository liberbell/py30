import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 4571))
    
    while True:
        msg = s.recv(1024)

        if not msg:
            print("No meesage from server. Closing the connection...")