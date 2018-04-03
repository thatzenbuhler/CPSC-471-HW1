#Client code
from socket import *

#Name and port number of the server
serverName = "localhost"
serverPort = 1234

#Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connect to server
clientSocket.connect((serverName, serverPort))

# A string to send to server
data = 'Hello world! This is a very long string.'

#Senddd ittt
bytesSent = 0
while bytesSent != len(data):
    bytesSent += clientSocket.send(data[bytesSent:])
                                   
#Close socket
clientSocket.close()
