import socket

UDP_IP_ADDRESS = "192.168.243.1"
UDP_PORT_NO = 20001
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    print("Waiting for message!")
    data, addr = serverSock.recvfrom(1024)
    print ("Message: ")
    print(data)