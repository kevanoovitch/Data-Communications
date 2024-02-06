# TCP Client TickTackToe
# Kevin Deshayes BTH
# Based on given example code


from socket import *
# serverName = 'hostname'
# Tries to use the webpage and DNS, otherwisee use this adress 46.30.213.174
serverName = 'www.ingonline.nu'
serverPort = 80

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# opens the TCP connection
clientSocket.connect((serverName, serverPort))

# Sends a custom and request the modified board
# Craft the requset and sends it

board = "xoxeeeoxo"
request = f"GET /tictactoe/index.php?board={board} HTTP/1.1\r\n" \
          "Host: www.ingonline.nu\r\n" \
          "Connection: close\r\n" \
          "User-agent: MyTicTacToeClient/1.0\r\n" \
          "\r\n"

clientSocket.send(request.encode())

# Print the received board
response = clientSocket.recv(1024)
print("Board: " + response.decode())

# close the TCP connection
clientSocket.close()
