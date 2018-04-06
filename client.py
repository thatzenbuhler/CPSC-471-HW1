#Client code
from socket import *
import os, sys

#Name and port number of the server
serverName = "localhost"
serverPort = 1234
contentPort = 2000

#Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)
contentSocket = socket(AF_INET, SOCK_STREAM)

#Connect to server
clientSocket.connect((serverName, serverPort))

# User menu for client
while True:
    print('ftp>', end='', flush=True)
    # splits user input so it can read multiple arguments
    word = input()
    words = word.split()
    if words[0] == "quit":
        break
    elif words[0] == "get":
        if len(words) == 1: continue
        filename = words[1]
        #search for filename; if found, download
        #if os.path.isfile(filename):
            
    elif words[0] == "ls":
        #list files on server
        clientSocket.send(words[0].encode())
    elif words[0] == "put":
        if len(words) == 1: continue
        filename = words[1]
        clientSocket.send((words[0] + " " + words[1]).encode())
        contentSocket.connect((serverName, contentPort))
        #opens file and stores data
        with open(filename) as file:
            data = file.read()
        file.closed
        data = data.encode()
        print("Sending file: ", filename)
        bytesSent = 0
        while bytesSent != len(data):
            bytesSent += contentSocket.send(data[bytesSent:])
        contentSocket.close()
#Close socket
clientSocket.close()
