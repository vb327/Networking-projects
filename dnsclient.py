#! /usr/bin/env python3
# DNS Client
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import time
import struct
import random

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
print("Sending Request to " + host + ", " + str(port) + ":")
mID = random.randint(1,100)
print("Message ID: " + str(mID))
question = str(hostname + " A IN")
quesLen = len(question)
print("Question Length: " + str(quesLen) + " bytes")
print("Answer Length: 0 bytes")
print("Question: " + question + "\n")

try:
    # Send data to server
    message = struct.pack('!HHIHH',1,0, mID, quesLen, 0)
    message2 = struct.pack('{}s'.format(quesLen), question.encode("UTF-8"))

    clientsocket.sendto(message,(host, port))
    clientsocket.sendto(message2,(host, port))

    # Receive the server response
    data, address = clientsocket.recvfrom(1024)
    result= struct.unpack('!HHIHH', data)
    data1, address = clientsocket.recvfrom(1024)
    result1 = struct.unpack('{}s'.format(len(data1)), data1)
    data2, address = clientsocket.recvfrom(1024)
    result2 = struct.unpack('{}s'.format(len(data2)), data2)
    print("Received response from "+ str(host) +" " + str(port) + ": ")
    if(result[1]==0):
        print("Return code: 0 (No errors)")
    else:
        print ("Return code: 1 (Name does not exist)")
    print("Message ID: " + str(result[2]))
    print("Question Length: " + str(result[3]) + " bytes")
    print("Answer Length: " + str(result[4]) + " bytes")
    print("Question: " + result1[0].decode("UTF-8"))
    if (result[4] != 0):
        print("Answer: " + result2[0].decode("UTF-8") + "\n")

except:
    for increment in range(2):
        print("Request timed out ...\nSending request to "+ host + ", " + str(port) + ":")
    print("Request timed out ... Exiting program.")

        #Close the client socket
clientsocket.close()
