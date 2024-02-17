import socket


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")

    while True:
        connection, address = server_socket.accept()
        print(f"Connection from {address}")
        connection.close()


if __name__ == "__main__":
    start_server(12000)  # Use the same port as your actual server
