class Connection:
    def __init__(self, tcp, addrs) -> None:
        self.tcp = tcp
        self.addrs = addrs
        self.msg = []

    def send(self, b: bytes) -> None:
        self.tcp.sendall(b)

    def recv(self) -> bytes:
        data = self.tcp.recv(256)
        return data

    def get_addrs(self):
        return self.addrs

    def disconnect(self) -> None:
        self.tcp.close()
