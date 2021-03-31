#! /usr/bin/env python3
# DNS Server
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import struct
import random

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
# loop forever listening for incoming UDP messages
lst = []
#ip = str()
#answer=str()
#returnCode = 1
file = open('dns-master.txt', 'r')
for line in file:
    if(line[0] != '#'):
        lst.append(line.rstrip('\n'))
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    result = struct.unpack('!HHIHH', data)
    data1, address = serverSocket.recvfrom(1024)
    result1 = struct.unpack('{}s'.format(len(data1)), data1)
    dec = result1[0].decode('UTF-8')
    domain = dec.split()[0]
    for line in lst:
        returnCode = 1
        answer = str()
        ip = str()
        if (domain in line):
            returnCode = 0
            split = line.split()
            ip = (split[-2] + " " + split[-1])
            answer = (dec+ " " + ip)
            break
    # Echo back to client

    ansLen = len(answer)
    message = struct.pack('!HHIHH', 2, returnCode, result[2], result[3], ansLen)
    serverSocket.sendto(message, address)
    message1 = struct.pack('{}s'.format(result[3]), dec.encode("UTF-8"))
    serverSocket.sendto(message1, address)
    message2 = struct.pack('{}s'.format(ansLen), answer.encode("UTF-8"))
    serverSocket.sendto(message2, address)
    answer = str()
    ansLen = 0
