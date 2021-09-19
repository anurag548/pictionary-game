"""
<<< MAIN THREAD >>>
Handles the request of the connection, creating new games and request from the clients
"""

import socket
import threading
import time
from .player import Player
from .game import Game
from queue import Queue


def player_thread(con, ip, name):



def authentication(conn, addr):
    """
    authentication
    :param ip:
    :return: None
    """
    try:
        data = conn.recv(16)
        name = str(data.decode())
        if not name:
            raise Exception("No name received")

        conn.sendall("1".encode())
        threading.Thread(target=player_thread, args=(conn, addr, name))
    except Exception as e:
        print("[EXCEPTION]", e)
        conn.close()


def connection_thread():
    server = ""
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("[CONNECT] New Connection!")

        authentication(addr)


if __name__ == '__main__':
    threading.Thread(target=connection_thread())