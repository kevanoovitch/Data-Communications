# TCP receiver


from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))


# Listen of incomming conenctions
serverSocket.listen(1)

print("The TCP server is ready to recieve", flush=True)

# Global Collectors
ErrorLog = []
ReceievedMSG = []
while True:
    # accept incomming connection
    connectionSocket, clientAdress = serverSocket.accept()
    print("Connection Received from:", clientAdress)

    try:
        while True:
            # read client's message and remember client's address (IP and port)
            message = connectionSocket.recv(2048)
            if not message:
                break  # if not message is received close the connection

            # Check Message ID
            nrOfMsg = 0
            MessageID = int(message.decode()[:5])
            nrOfMsg += 1

            # Error checking
            if ReceievedMSG:  # List is not empty
                lastMessage = ReceievedMSG[-1]
                # If current message ID is smaller than previous
                if MessageID < lastMessage:
                    error = f"{MessageID} was smaller than previous ({ReceievedMSG[nrOfMsg -1 ]})"
                    ErrorLog.append(error)
                # If current message is bigger than expected
                if MessageID > ReceievedMSG[nrOfMsg - 1] + 1:
                    error = f"{MessageID} was bigger than expected ({ReceievedMSG[nrOfMsg -1 ]})"
                    ErrorLog.append(error)

            # Print message and client address
            print(message.decode())

            ReceievedMSG.append(MessageID)

            # Print Result of data transfer
            if len(ErrorLog) == 0:
                print("no errors")
                connectionSocket.send("ok".encode())
            else:
                print("erros found!")

            for error in ErrorLog:
                print(f"{error} \n")

            print("<--- All MessageIDs in received order -- >")
            for MessageID in ReceievedMSG:
                print(f"{MessageID}\n")

    finally:
        connectionSocket.close()
