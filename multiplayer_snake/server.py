import socket
from time import sleep

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:
    data = conn.recv(1024)
    print(f'Received {data} from {addr}')
    if data == b'':
        break
    sleep(3)
    reply = b'Odpoved: ' + data
    conn.sendall(reply)
    print(f'Sent {reply} to {addr}')
conn.close()

s.close()
