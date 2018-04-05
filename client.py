#Client code
from socket import *
import os, sys

#Name and port number of the server
serverName = "localhost"
serverPort = 1234

#Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connect to server
clientSocket.connect((serverName, serverPort))

# A string to send to server
data = "Hello world! This is a very long string."
data = data.encode()

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
        if os.path.isfile(filename):
            download = open(filename, "wb")
            #while loop till all bytes are recvd
           
            #way number 1, just receives with a buffer of 1024 infinitely i believe
            while True:
                downData = clientSocket.recv(1024)
                if not data:
                    break
                download.write(data)
            download.close()
         
            #way number 2, try to get file size
            #should return filesize to data size
            dataSize = os.path.getsize(filename)
            #buffer
            downData = ""
            #tmp buffer
            movData = ""
            #recv till all is recvd
            while len(downData) < dataSize:
                movData = clientSocket.recv(dataSize)
                #server has closed the socket
                if not movData:
                    break
                #append the received bytes to the buffer
                downData += tmpData
                download.write(downData)
            download.close
            
    elif words[0] == "ls":
        #list files on server
        test = 0
    elif words[0] == "put":
        if len(words) == 1: continue
        filename = words[1]
        print("Sending file: ", filename)
        bytesSent = 0
        # add file.open functionality. Currently resends earlier string
        while bytesSent != len(data):
            bytesSent += clientSocket.send(data[bytesSent:])


#Senddd ittt
#bytesSent = 0
#while bytesSent != len(data):
#    bytesSent += clientSocket.send(data[bytesSent:])
                                   
#Close socket
clientSocket.close()
