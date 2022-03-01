import socket
import connection

from threading import Thread

class ConnectionManager:

    def __init__(self, ip_addres: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip_addres, port))
        self.clients = []
        self.acception = None
        self.recvpool = None
        self.running = False;

    def start(self) -> None:
        self.running = True;
        self.sock.listen()
        self.acception = Thread(target=self.__acception)
        self.acception.start()
        self.recvpool = Thread(target=self.__recv_pool)
        self.recvpool.start()

    def __acception(self) -> None:
        while self.running:
            tcp, addrs = self.sock.accept()
            conn = connection.Connection(tcp, addrs)
            self.clients.append(conn)
            print(f"Client connected: {addrs}")

    def broadcast(self, msg: str) -> None:
        bts = str.encode(msg)
        for client in self.clients:
            client.send(bts)

    def __recv_pool(self) -> None:
        while self.running:
            for client in self.clients:
                buffer = self.__recv(client)
                if not buffer:
                    self.disconnect(client)
                else:
                    print(
                        f"Client :{client.get_addrs()} | message: {buffer.decode()}")

    def __recv(self, client) -> bytes:
        buffer = client.recv()
        return buffer

    def disconnect(self, client) -> None:
        print(f"Client {client.get_addrs()} disconnected.")
        client.disconnect()
        self.clients.remove(client)

    def close(self):
        for client in self.clients:
            self.disconnect(client)
        self.running = False
        self.acception.join()
        self.recvpool.join()

