# UDP receiver


from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The UDP server is ready to recieve", flush=True)

# Global Collectors
ErrorLog = []
ReceievedMSG = []

while True:
    # read client's message and remember client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)

    # Check Message ID
   
    MessageID = int(message.decode()[:5])
    


# Error checking
    if ReceievedMSG:  # List is not empty
        lastMessage = ReceievedMSG[-1]
        # If current message ID is smaller than previous
        if MessageID < lastMessage:
            error = f"{MessageID} was smaller than previous ({ReceievedMSG[-1]})"
            ErrorLog.append(error)
        # If current message is bigger than expected
        if MessageID > ReceievedMSG[-1] + 1:
            error = f"{MessageID} was bigger than expected ({ReceievedMSG[-1 ]})"

    # Print message and client address
    print(message.decode())
    print(clientAddress)

    ReceievedMSG.append(MessageID)

    # Print Result of data transfer
    if len(ErrorLog) == 0:
        print("no errors")
        
    else:
        print("erros found!")

        for error in ErrorLog:
            print(f"{error} \n")

        print("<--- All MessageIDs in received order -- >")
        for MessageID in ReceievedMSG:
            print(f"{MessageID}\n")

        break  # Stops reciver when erros have been detected
