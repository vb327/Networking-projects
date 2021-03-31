#! /usr/bin/env python3
# HTTP Client
#Viktoriya Buldiak; vb327; CS356-012
import sys
import socket
import time
import os.path
# Get the web url as command line argument
url = sys.argv[1]
host = url.split('/')[0]
hostname = host.split(':')[0]
port = host.split(':')[1]
file = (url.split('/')[1])

# Create UDP client socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((hostname,int(port)))
#get statements
get = "GET /"+str(file) + " HTTP/1.1\r\nHost: " + str(host) + "\r\n"
#given file
if os.path.isfile(file):
    f = open(file).read()
    secs = os.path.getmtime(file)
    tim = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", tim)
cache = ""
#cache file
if not os.path.isfile('cache.txt'):
    cache = open('cache.txt', 'x')
cache = open('cache.txt', 'r')
#if not cached
if os.path.isfile(file):
    if file not in cache.read():
        print(get)
        add = open('cache.txt', 'w')
        add.write(file+'\n' + f+'\n')
    else:
        get = (get + "If-Modified-Since: " + str(last_mod_time) + "\r\n")
        print(get)
#no file
else:
    print(get)

clientsocket.send(get.encode('utf-8'))
# Receive the server response
data = clientsocket.recvfrom(2048)
received = data[0].decode('utf-8')
print(received)

#Close the client socket
clientsocket.close()
