# TCP Sender


from socket import *
import time
import random


def splitIntoPackets(data, size):
    packets = []
    for i in range(0, len(data), size):
        packets.append(data[i:i+size])

    return packets


# Ask for input
flag = False
while not flag:
    print("Please choose messages sent interval")
    print("a = 1 msg / 10 seconds")
    print("b = 1 msg / 1 seconds")
    print("c = 1 msg / 0.25 seconds")
    print("d = custom")
    answer = input()

    if answer in ["a", "b", "c", "d"]:
        flag = True
        if answer == "a":
            messagesInterval = 0.1
        elif answer == "b":
            messagesInterval = 1
        elif answer == "c":
            messagesInterval = 4
        elif answer == "d":
            messagesInterval = input("Enter custom value (int): ")
            while messagesInterval.isdigit() == False:
                messagesInterval = input("error try again: ")
            messagesInterval = int(messagesInterval)

    else:
        print("Wrong input, please type a, b or c then enter")


# Parameters
max_bytes = 1470
duration = 100  # Seconds


# serverName = 'hostname'
serverName = "localhost"

serverPort = 12000

# create TCP socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to TCP server
sock.connect((serverName, serverPort))
print("Connection established")

# read from file
f = open("UDPStream.txt", "rb")
Contents = f.read()
f.close()

# split into equal packages

PacketsList = splitIntoPackets(Contents, max_bytes)

# Ask for to send in debug/fake mode
fakeMode = False
while True:
    print("Do you want to run in fake send mode? Y/N ")
    answer = input()

    if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
        flag = True
        if answer == "Y" or answer == "y":
            fakeMode = True
            break
        elif answer == "N" or answer == "n":
            fakeMode = False
            break
    else:
        print("Wrong input, please Y/N then enter")

# ask for streaming parameter
while True:
    print("Do you want to run set max duration to 20s? (default 100s) Y/N ")
    answer = input()

    if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
        if answer == "Y" or answer == "y":
            duration = 20
            break
        elif answer == "N" or answer == "n":
            break
    else:
        print("Wrong input, please Y/N then enter")

# calculate interval and start time
startTime = time.time()
interval = 1.0 / messagesInterval


# Send while less seconds from start has gone that set duration

MessageID = 10001

MessagesSent = 0
for packet in PacketsList:
    if time.time() - startTime > duration:
        break

    DataPayload = str(MessageID) + str(packet) + "####"
    sock.send(DataPayload.encode())
    if (fakeMode == True):
        MessageID = 10000 + random.randint(1, len(PacketsList))
    else:
        MessageID += 1
    MessagesSent += 1

    time.sleep(interval)  # Takes a "paus" between the msg being sent




# close TCP socket
sock.close()
