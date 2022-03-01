class Connection:
    def __init__(self, tcp, addrs) -> None:
        self.tcp = tcp
        self.addrs = addrs

    def send(self, b: bytes)-> None:
       self.tcp.sendall(b) 
        
