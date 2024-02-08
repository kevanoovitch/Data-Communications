# UDP Sender


from socket import *
import time


def splitIntoPackets(data, size):
    packets = []
    for i in range(0, len(data), size):
        packets.append(data[i:i+size])

    return packets


# Parameters
max_bytes = 1470
duration = 1  # Seconds
msgPerSecond = 1

# serverName = 'hostname'
serverName = "localhost"

serverPort = 12000

# create UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

# read from file
f = open("UDPData.txt", "rb")
Contents = f.read()
f.close()

# split into equal packages

PacketsList = splitIntoPackets(Contents, max_bytes)

startTime = time.time()
interval = 1.0 / msgPerSecond


# Send while less seconds from start has gone that set duration

MessageID = 10001

lastMessageID = len(PacketsList) + MessageID
allPacketsSent = False
while time.time() - startTime < duration and allPacketsSent == False:

    for i in range(0, len(PacketsList)):
        if MessageID <= lastMessageID:
            DataPayload = str(MessageID) + str(PacketsList[i]) + "####"
            sock.sendto(DataPayload.encode(), (serverName, serverPort))
            MessageID += 1
        else:
            allPacketsSent = True
            break  # Break the loop when all is sent

    time.sleep(interval)  # Takes a "paus" between the msg being sent


response, serverAddress = sock.recvfrom(2048)

# output modified sentence and close the socket, cast message to string
print("Received from server: ", response.decode())

# close UDP socket
sock.close()
