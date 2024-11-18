import socket
import threading
import time

# Server Code
def run_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to localhost and port 12345
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on localhost:12345...")

    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    # Receive a message from the client
    client_message = client_socket.recv(1024).decode()
    print(f"Client says: {client_message}")

    # Send a reply to the client
    server_message = "Hello from the Server!"
    client_socket.send(server_message.encode())

    # Close the connection
    client_socket.close()
    server_socket.close()

# Client Code
def run_client():
    # Give the server a moment to start
    time.sleep(2)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))
    print("Connected to server localhost:12345")

    # Send a message to the server
    client_message = "Hello from the Client!"
    client_socket.send(client_message.encode())

    # Receive a reply from the server
    server_message = client_socket.recv(1024).decode()
    print(f"Server says: {server_message}")

    # Close the connection
    client_socket.close()

# Run both Server and Client using threading
server_thread = threading.Thread(target=run_server)
client_thread = threading.Thread(target=run_client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()