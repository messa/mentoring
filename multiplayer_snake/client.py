# Echo client program
import socket
from time import sleep

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = b'Hello, world'
    s.sendall(data)
    print(f'Sent: {data}')
    data = s.recv(1024)
    print(f'Received: {data}')
    sleep(2)

s.close()
