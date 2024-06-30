import socket
import threading
import sys
from crypto_utils import encrypt_message, decrypt_message

# Khóa AES (phải giống với khóa trên máy chủ)
aes_key = b'1234567890abcdef'  # 16 byte key

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decrypted_message = decrypt_message(message, aes_key)
            if decrypted_message.startswith("SYS:"):
                print(f"\n{decrypted_message[4:]}")
            elif decrypted_message.startswith("MSG:"):
                print(f"\nReceived from {decrypted_message[4:]}")
            else:
                print(f"\nReceived: {decrypted_message}")
            print("Enter message: ", end="", flush=True)  # In lại "Enter message:" sau khi nhận tin nhắn
        except:
            print("Connection lost")
            client_socket.close()
            break

def send_name(client_socket):
    name = input("Enter your name: ")
    encrypted_name = encrypt_message(f"NAME:{name}", aes_key)
    client_socket.send(encrypted_name)
    confirmation_message = client_socket.recv(1024)
    decrypted_confirmation = decrypt_message(confirmation_message, aes_key)
    print(f"\n{decrypted_confirmation}")
    print("Enter message: ", end="", flush=True)

def send_messages(client_socket):
    while True:
        try:
            message = input()
            if not message:
                continue
            encrypted_message = encrypt_message(message, aes_key)
            print(f"Encrypted message: {encrypted_message}\n")
            client_socket.send(encrypted_message)
            print("Enter message: ", end="", flush=True)
        except KeyboardInterrupt:
            print("Client shutting down...")
            client_socket.close()
            break

# Thiết lập kết nối khách hàng
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# Yêu cầu người dùng nhập tên và xác nhận
send_name(client_socket)

# Bắt đầu luồng để nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Bắt đầu luồng để gửi tin nhắn
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()

# Đợi cả hai luồng hoàn thành
receive_thread.join()
send_thread.join()
