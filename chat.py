import socket
import threading
import os

HEADER = 64
PORT = 5351
SERVER = "192.168.0.47"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!D"

IPS = []
USERNAMES = []

Messages = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

open("messages.txt", "w")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    IPS.append(addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            Messages.append(f"{addr} : {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print("| !DISCONNECTED FROM CHAT! |")

            print(f"[{addr}] {msg}")

            with open("messages.txt", "r") as file:
                pf = file.read()

                with open("messages.txt", "w") as f:
                    f.write("")

                with open("messages.txt", "a") as f:
                    f.write(f"{addr} >  {msg}")
                    f.write(str(pf))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING SERVER]")
start()




