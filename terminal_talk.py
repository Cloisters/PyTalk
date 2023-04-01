import socket

# Set up socket connection
HOST = 'localhost'  # The remote host (change this to the IP address of the receiving terminal)
PORT = 1111        # The same port as used by the receiving terminal
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Send text input to receiving terminal
while True:
    message = input("Type a message to send: ")
    s.sendall(message.encode())
