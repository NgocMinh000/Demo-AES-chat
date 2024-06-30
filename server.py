import socket
import threading
from crypto_utils import generate_aes_key, encrypt_message, decrypt_message

# Khóa AES
aes_key = b'1234567890abcdef'  # 16 byte key

# Thiết lập máy chủ
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

clients = []
client_names = {}

def broadcast(message, client_socket, sender_name):
    for client in clients:
        if client != client_socket:
            try:
                client.send(encrypt_message(f"MSG:{sender_name}: {message}", aes_key))
            except:
                clients.remove(client)
                client.close()

def handle_client(client_socket):
    name = ""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decrypted_message = decrypt_message(message, aes_key)
            if decrypted_message.startswith("NAME:"):
                name = decrypted_message.split(":", 1)[1]
                client_names[client_socket] = name
                print(f"User {name} connected")
                success_message = f"User Name {name} connected successfully."
                client_socket.send(encrypt_message("SYS:" + success_message, aes_key))
            else:
                print(f"Received from {name}: {decrypted_message}")
                broadcast(decrypted_message, client_socket, name)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def receive():
    while True:
        try:
            client_socket, addr = server.accept()
            clients.append(client_socket)
            print(f"Connection established with {addr}")
            threading.Thread(target=handle_client, args=(client_socket,)).start()
        except:
            print("Error accepting connection")
            break

print("Server is running...")
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Đợi luồng chính không kết thúc
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Server shutting down...")
    for client in clients:
        client.close()
    server.close()
    receive_thread.join()
