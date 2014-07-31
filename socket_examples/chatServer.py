#!/usr/bin/python

from socket import *
import thread

HOST = ''
PORT = 8888
BUFFER = 1024
ADD = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADD)
serverSocket.listen(5)

def reception(client):
    while True:
        rcvdPackage = clientSocket.recv(1024)
        print "%s >> %s \n" %(client, rcvdPackage)
        thread.start_new_thread(sending,())

def sending():
    while True:
        msg = raw_input("Me >> ")
        clientSocket.send(msg)

while True:
	print 'Waiting....'
    	clientSocket, clientAdd = serverSocket.accept()
        print "Connected"
        server = clientSocket.send("server")
        client = clientSocket.recv(BUFFER)
        thread.start_new_thread(reception(client),())

clientSocket.close()
serverSocket.close()
