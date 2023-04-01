import socket

# Set up socket connection
HOST = 'localhost'  # The local host (change this to the IP address of the sending terminal)
PORT = 1111        # The same port as used by the sending terminal
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

# Receive text input from sending terminal
print("Waiting for messages...")
conn, addr = s.accept()
with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received message: {data.decode()}")
