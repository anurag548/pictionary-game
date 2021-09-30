import socket
import json
import time as t


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.105.63.92"
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
            while 1:
                last = self.client.recv(1024).decode()
                di += last
                try:
                    if di.count(".") == 1:
                        break
                except:
                    pass
            #print(di)
            try:
                if di[-1] == ".":
                    di = di[:-1]
            except:
                pass
            keys = [key for key in data.keys()]
            return json.loads(di)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] disconnected from the server", msg)
        self.client.close()

