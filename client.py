import socket


class connect:
    def __init__(self, address: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port

    def __enter__(self):
        self.socket.connect((self.address, self.port))
        return self.socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()


HOST, PORT = "localhost", 8000
with connect(address=HOST, port=PORT) as sock:
    while True:
        message = input("> ")
        sock.sendall(message.encode("utf-8"))
        response = sock.recv(1024).decode("utf-8")
        print(response)
