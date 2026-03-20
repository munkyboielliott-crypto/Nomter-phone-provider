import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0", 12345))  # important for Render
    server.listen()

    print("Server is running...")

    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")

        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

start_server()
