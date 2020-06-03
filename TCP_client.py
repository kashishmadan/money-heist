# Designed by Kashish Madan
# Manipal University Jaipur
# 179202069 
# Date 03-06-2020

import socket
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.243.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print("            *")
print("          * * *")
print("        * * * * * ")
print("      * * * * * * * ")
print("    * * * * * * * * * ")
print("  * * * * * * * * * * * ")
print("* * * * * * * * * * * * * ")
print("* * *               * * * ")
print("* * *               * * * ")
print("* * *               * * * ")
print("WELCOME")
print("THIS IS RELIABLE NETWORK")
print("FOR PROFESSOR & POLICE/RAQUEL MURILLO")
print("Let's Start!")
while True:
    print("Type your message here: (type DISCONNECT to disconnect)")
    datam = input()
    if(datam=="DISCONNECT"):
        send(DISCONNECT_MESSAGE)
        break
    send(datam)
    print("Send random text for header: ")
    input()