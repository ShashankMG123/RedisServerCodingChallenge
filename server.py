import socket
import threading
from commands import redisCommands

PORT = 6379
SERVER = "localhost"
ADDR = (SERVER, PORT)

FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break
            if msg == "quit":
                connected = False
            print(f"{addr}: {msg}")

            response = redisCommandsSet.driver(msg)
            if response == "Invalid arg":
                return "-Error Message\r\nInvalid command\r\n"
            conn.send(bytes(response, FORMAT))

        print(f"Closing connection with client")
        conn.close()
    except:
        conn.close()

def start():
    try:
        print("[SERVER STARTED]!")
        server.listen()
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except:
        server.close()

redisCommandsSet = redisCommands()
start()
