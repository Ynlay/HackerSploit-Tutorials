import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.7'
host = socket.gethostname()

port = 444 

clientSocket.connect(host, port)

message = clientSocket.recv(1024)

clientSocket.close()

print(message.decode('ascii'))

# ADD THIS TO A VIRTUAL MACHINE OR JUST A DIFFERENT MACHINE 