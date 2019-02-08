import socket

# Creating the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444 

# Binding to socket
# Host will be replaced/substituted with IP, 
# if changed and not running on host
serverSocket.bind(host, port) 

# Starting TCP listener
serverSocket.listen(3)

while True: 
    # Starting the Connection
    clientSocket, address = serverSocket.accept()

    print("Received connection from %s " % str(address))

    message = "Hello! Thank you for connecting to the server!" + "\r\n"
    clientSocket.send(message.encode('ascii'))

    clientSocket.close()

