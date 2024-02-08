# UDP receiver


from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The UDP server is ready to recieve", flush=True)

while True:
    # read client's message and remember client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)

    # Print message and client address
    print(message.decode())
    print(clientAddress)

    # send back modified sentence to client using remembered address
    serverSocket.sendto("ok".encode(), clientAddress)
