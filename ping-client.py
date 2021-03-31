#! /usr/bin/env python3
# Ping Client
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import time
import struct

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])

pTrans=int(0)
pRec=int(0)
RTTlist = []

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
print("Pinging " + host + ", " + str(port) + ":")
for increment in range(1,11):
    try:
        # Send data to server
        message = struct.pack('!HH',1,increment)
        start = time.time()
        clientsocket.sendto(message,(host, port))


        # Receive the server response
        data, address = clientsocket.recvfrom(1024)
        end = time.time()
        RTT = round(end-start, 6)
        RTTlist.append(RTT)
        result= struct.unpack('!HH', data)
        print("Ping message number "+ str(increment) + " RTT: " + str(RTT))
        pRec+=1

    except:
        print("Ping message number " + str(increment) + " timed out")

average = (sum(RTTlist)/len(RTTlist))
lost = (10 - pRec)*10
print("\nStatistics:\n10 packets transmitted, " + str(pRec) + " received, " + str(lost) + "% packet loss")
print("Min/Max/Av RTT = "+ str(min(RTTlist)) +" / " + str(max(RTTlist)) + " / " + str(round(average,6)))
        #Close the client socket
clientsocket.close()
