#! /usr/bin/env python3
# HTTP Server
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import time
import os.path

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mod = "If-Modified-Since"
# get current time
current = time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", time.gmtime())

#get modified time
def checkModTime(file):
    secs = os.path.getmtime(file)
    tim = time.gmtime(secs)
    return time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", tim)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
while True:
    client, data  = serverSocket.accept()

    # Receive the client data
    data = client.recvfrom(1024)
    decoded = data[0].decode('utf-8')
    filename = decoded.split('/')[1].split(' ')[0]
    if not os.path.isfile(filename):
        answer = ("HTTP/1.1 404 Not Found\r\nDate: "+current+"Content-Length: 0\r\n\r\n")
    else:
        inFile = open(filename,'r')
        file = inFile.read()
        #inFile.close()
    #get then size of a file
        blen = os.path.getsize(filename)
        if not mod in decoded:
            answer = ("HTTP/1.1 200 OK\r\nDate: " + current + "Last-Modified: " + str(checkModTime(filename)) + "Content-Length: " + str(blen) + "\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"+file)
        elif mod in decoded:
            fileModTime = decoded.split(mod + ': ')[1]
            cacheMod = checkModTime("cache.txt")
            if (cacheMod > fileModTime):
                answer = ("HTTP/1.1 304 Not Modified\r\nDate: "+ current +'\r\n\r\n')
            else:
                answer = ("HTTP/1.1 200 OK\r\nDate: " + current + "Last-Modified: " + str(checkModTime(filename)) + "Content-Length: " + str(blen) + "\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"+file)

    client.send(answer.encode('utf-8'))
