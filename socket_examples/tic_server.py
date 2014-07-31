#!/usr/bin/python

#TODO
# 1. Restart game option.

#BUGS
# 1. Crashes on empty or invalid input.

import socket

HOST = '10.42.43.1'
PORT = 8888
BUFFER = 1024
ADD = (HOST, PORT)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ADD)
serverSocket.listen(5)

cell = [" "," "," "," "," "," "," "," "," "]

p1 = []
p2 = []
occupied = []
pid = 1

def display(cell):
    #Artwork of the board.
    print '''\t\t %s | %s | %s  
    \t\t-----------
    \t\t %s | %s | %s 
    \t\t-----------
    \t\t %s | %s | %s 
    ''' %(cell[0], cell[1], cell[2], cell[3], cell[4], cell[5], cell[6], cell[7], cell[8])
    
def layout():
    #Displays the layout of the board.
    print "LAYOUT:"
    plan = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    display(plan)
    
def play():
    #Input is taken here.
    if pid == 1:
        ip = input("Player 1, enter your choice: ")
        clientSocket.send(str(ip))
        if ip in range(0,9):
            if ip in occupied:
                print "Cell already occupied. Enter another choice."
                play()
            else:
                occupied.append(ip)
                p1.append(ip)
                position(ip)
        else:
            print "Error! Enter a valid choice."
            play()
    else:
        print "Player 2's turn...'"
        r = clientSocket.recv(BUFFER)
        ip = int(r)
        if ip in range(0,9):
            if ip in occupied:
                print "Cell already occupied. Enter another choice."
                play()
            else:
                occupied.append(ip)
                p2.append(ip)
                position(ip)
        else:
            print "Error! Enter a valid choice."
            play()
    
def win(ip_seq):
    #Decides the winner.
    win = 0
    win_seq = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
    for i in range (0, len(win_seq)):
        part = win_seq[i]
        if cell[part[0]] == cell[part[1]] == cell[part[2]] == "X":
            print "Player 1 wins the game."
            win = 1
            terminate()
        elif cell[part[0]] == cell[part[1]] == cell[part[2]] == "O":
            print "Player 2 wins the game."
            win = 1
            terminate()
        elif len(occupied)==9 and win == 0:
            print "Game draw."
            terminate()
        else:
            pass

def position(pos):
    #Places the appropriate letter in appropriate block.
    if pid == 1:
        cell[pos] = "X"
        display(cell)
    else:
        cell[pos] = "O"
        display(cell)
    
def terminate():
    #Closes the connection and exits the program.
    serverSocket.close()
    exit()
            

 
#Creates the socket and waits for client to connect.
while True:
	print 'Waiting....'
    	clientSocket, clientAdd = serverSocket.accept()
        print "Connected"
        break

#Main loop starts here.
layout()
while True:
    pid = 1
    play()
    if len(p1) >= 3:
        win(p1)
    pid = 2
    play()
    if len(p2) >= 3:
        win(p2)


