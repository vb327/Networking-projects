#! /usr/bin/env python3
# Ping Server
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import struct
import random
import time

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
seq = int(0)
# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")
#put time.sleep(0.01)
# loop forever listening for incoming UDP messages
ran = random.randint(1,10)
while True:

        seq+=1
        # Receive and print the client data from "data" socket
        data1, address1 = serverSocket.recvfrom(1024)
        time.sleep(0.01)
        result = struct.unpack('!HH', data1)
        if (result[1] !=ran):

            # Echo back to client
            print("Responding to ping request with sequence number "+ str(result[1]))
            message = struct.pack('!HH', 2, result[1])
            serverSocket.sendto(message, address1)
            ran = random.randint(1,10)
        else:
            print("Message with sequence number " + str(result[1]) + " dropped")
