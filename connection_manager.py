import socket
import connection

from threading import Thread

class ConnectionManager:
    def __init__(self, ip_addres: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.sock.bind((ip_addres, port));
        self.clients = []
        self.thread = None;

    def start(self) -> None:
        self.sock.listen()
        self.thread = Thread(target= self.__acception)

    def __acception(self) -> None:
        while True:
            tcp, addrs = self.sock.accept()
            conn = connection.Connection(tcp, addrs)
            self.clients.append(conn)
            print(f"Client connected: {addrs}")

    def broadcast(self, msg: str) -> None:
        for connect in self.clients:
            connect.send(msg.encode)
                

