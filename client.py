#Client code
from socket import *
import os, sys


#Name and port number of the server (no user arg given)
serverName = "localhost"
serverPort = 1234
contentPort = 2000
reversePort = 2001

#Change ports to user arg
if len(sys.argv) == 3:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    contentPort = serverPort + 1
    reversePort = contentPort + 1

# User menu for client
while True:
    #Connect or reconnect to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print('ftp>', end='', flush=True)
    # splits user input so it can read multiple arguments
    word = input()
    words = word.split()
    if words[0] == "quit":
        clientSocket.send(words[0].encode())
        break
    elif words[0] == "get":
        #Send command and filename to search from server
        if len(words) == 1: continue
        filename = words[1]
        clientSocket.send((words[0] + " " + words[1]).encode())
        #Attempt to start a server-like connection to receive file
        recvSocket = socket(AF_INET, SOCK_STREAM)
        recvSocket.bind(('', reversePort))
        recvSocket.listen(1)
        connect2, addr2 = recvSocket.accept()
        content = connect2.recv(1024)
        print(content.decode())
        connect2.close()
    elif words[0] == "ls":
        #list files on server
        clientSocket.send(words[0].encode())
    elif words[0] == "put":
        if len(words) == 1: continue
        filename = words[1]
        clientSocket.send((words[0] + " " + words[1]).encode())
        contentSocket = socket(AF_INET, SOCK_STREAM)
        contentSocket.connect((serverName, contentPort))
        #Opens file and sends data over contentSocket
        with open(filename) as file:
            data = file.read()
        file.closed
        data = data.encode()
        print("Sending file: ", filename)
        bytesSent = 0
        while bytesSent != len(data):
            bytesSent += contentSocket.send(data[bytesSent:])
        contentSocket.close()
    clientSocket.close()
#Close final connection
clientSocket.close()
