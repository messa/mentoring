import socket
from time import sleep

HOST = 'www.seznam.cz'    # The remote host
PORT = 80              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = b'GET / HTTP/1.0\r\nHost: www.seznam.cz\r\n\r\n'
s.sendall(data)
print(f'Sent: {data}')
data = s.recv(1024)
#print(f'Received: {data}')
print(data.decode('utf-8'))

s.close()
