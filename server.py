import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []


def send_to_all(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            send_to_all(message)
        except:
            break

    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        username = names.pop(index)
        send_to_all(f"{username} left the chat.".encode())
    client.close()


def receive_clients():
    print("Server is running...")

    while True:
        client, address = server.accept()
        print(f"Connected: {address}")

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        names.append(username)

        print(f"{username} joined the chat.")
        send_to_all(f"{username} joined the chat.".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive_clients()