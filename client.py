import socket
import time

PORT = 6379
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    connection = connect()
    while True:
        msg = input("% redis-cli ")
        send(connection, msg)
        if(msg == "quit"):
            break
        data = connection.recv(1024).decode()
        print(data)



start()