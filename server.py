# Server code
from socket import *

# The port on which to l i s t e n
serverPort = 1234

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to the port
serverSocket.bind(('', serverPort))

# S t art l i s t e n i n g f or incoming connections
serverSocket.listen(1)
print ("The server is ready to receive")

# The b u f f e r to s t o r e the r received data
#data = 0

# Forever accept incoming connections
while 1 :
    # Accept a connection ; get client’s socket
    connectionSocket , addr = serverSocket.accept()
    # Receive whatever the newly connected client has to send
    data = connectionSocket.recv(1000)
        
    print(data.decode())
    # Close the socket
    connectionSocket.close()
