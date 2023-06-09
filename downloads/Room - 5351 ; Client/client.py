import socket

HEADER = 64
PORT = 5351
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!D"
SERVER = "xenonium.duckdns.org"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("| !CONNECTED! |")
print("| COMMANDS [!D - disconnect from room] |")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    send_msg = input()
    if send_msg != "":
        send(send_msg)
    else:
        pass
