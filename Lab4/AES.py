from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import hashlib

sender_password = input("Enter Sender key: ")
receiver_password = input("Enter Receiver key: ")

if not sender_password or not receiver_password:
    print("Error: Keys can not be empty!")
    exit()

sender_key = hashlib.sha256(sender_password.encode()).digest()
receiver_key = hashlib.sha256(receiver_password.encode()).digest()

print("\nEnter sender AES key:", sender_key.hex())
print("Enter receiver AES key:", receiver_key.hex())
print("Key length is:", len(sender_key) * 8, "bits")

if sender_key != receiver_key:
    print("\nError: Sender and Receiver keys do not match!")
    exit()

print("\nKeys match: True")

message = input("\nEnter message: ")

nonce = os.urandom(12)
aes_sender = AESGCM(sender_key)

encrypted = aes_sender.encrypt(
    nonce, message.encode(), None
)

print(f"Inicialized vector: {nonce}")
print("\nOriginal :", message)
print("Encrypted :", encrypted.hex())

aes_receiver = AESGCM(receiver_key)

decrypted = aes_receiver.decrypt(
    nonce, encrypted, None
)

print("Decrypted:", decrypted.decode())
