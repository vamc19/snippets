#!/usr/bin/python

from socket import *
import thread

HOST = '127.0.0.1'
PORT = 8888
ADD = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADD)
client = clientSocket.send("client")
server = clientSocket.recv(1024)

def reception():
    while True:
        data = clientSocket.recv(1024)
        print "%s >> %s \n" %(server, data)

while True:
    sentPackage = raw_input("Me >> ")
    clientSocket.send(sentPackage)
    thread.start_new_thread(reception, ())
clientSocket.close()

