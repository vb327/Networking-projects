#! /usr/bin/env python3
# Echo Client

import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count # Initialize data to be sent

# Create UDP client socket.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(0.7)
for increment in range (3):
    try:
        # Send data to server
        print("Sending data to   " + host + ", " + str(port) + ": " + data)
        clientsocket.sendto(data.encode(),(host, port))

        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(1024)

    except:
        print("Message timed out")
    else:
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break

#Close the client socket
clientsocket.close()
