# Server code
from socket import *
import os, sys

# The port on which to listen
serverPort = 1234
contentPort = 2000

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
contentSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to the port
serverSocket.bind(('', serverPort))
contentSocket.bind(('', contentPort))

# Start listening for incoming connections
#serverSocket.listen(1)
print ("The server is ready to receive")

# Forever accept incoming connections
while 1 :
    serverSocket.listen(1)
    # Accept a connection ; get client’s socket
    connectionSocket , addr = serverSocket.accept()
    # Receive whatever the newly connected client has to send
    menu = connectionSocket.recv(1024)
    menu = menu.decode()
    menu = menu.split()
    print(menu)
    if menu[0] == "put":
        contentSocket.listen(1)
        connect2, addr2 = contentSocket.accept()
        content = connect2.recv(1024)
        print(content.decode())
        connect2.close()
    elif menu[0] == "ls":
        print("Files in server directory:")
        for file in os.listdir():
            print(file)
    # Close the socket
    connectionSocket.close()
