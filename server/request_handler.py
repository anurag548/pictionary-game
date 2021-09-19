"""
<<< MAIN THREAD >>>
Handles the request of the connection, creating new games and request from the clients
"""

import socket
from _thread import *
import time
from .player import Player
from queue import Queue
