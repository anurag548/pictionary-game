import socket
import json


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5556
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())
            di = ""
            last = 1
            while last:
                last = self.client.recv(1024).decode()
                di += last
            print(di)
            return json.loads(self.client.recv(2000000).decode())
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] disconnected fromm the server", msg)
        self.client.close()


n = Network("Player One")
print(n.send({3: []}))
