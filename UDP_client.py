import socket
#import codecs
UDP_IP_ADDRESS = "192.168.243.1"
UDP_PORT_NO = 20001
while True:
    print("Enter your message: (Press DISCONNECT to disconnect) ")
    msg = input()
    if(msg=="DISCONNECT"):
        break
    #message = codecs.encode(msg)
    message = msg.encode()
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))