import socket

host = "127.0.0.1"
port = 7171

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
while True:
    msg = sock.recv(256)
    if not msg:
        sock.close()
        break
    else:
        print(msg.decode())
        sock.sendall(msg)