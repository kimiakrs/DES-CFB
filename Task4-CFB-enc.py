#KimiaSadatKarbasi-SID60393958
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import os
import binascii

def main():
    plaintext_path = '/opt/DES/Task4/plain.txt'    # Input file to encrypt
    ciphertext_path = '/opt/DES/Task4/cipher.txt'  # Output encrypted file
    key_path = '/opt/DES/Task4/key.txt'           # File to store encryption keys


    # Read plaintext (try both UTF-8 and binary fallback)
    try:
        with open(plaintext_path, 'r', encoding='utf-8') as f:
            plaintext = f.read().encode('utf-8')
    except UnicodeDecodeError:
        with open(plaintext_path, 'rb') as f:
            plaintext = f.read()

    # Generate cryptographic material
    key = get_random_bytes(8)  # DES uses 56-bit key + 8 parity bits
    iv = get_random_bytes(8)   # Initialization Vector (block size)

# Initialize DES in CFB mode
# - key: Our generated encryption key
# - MODE_CFB: Cipher Feedback Mode selection
# - iv: Initialization Vector
# - segment_size=8: Process 8 bits (1 byte) at a time
    cipher = DES.new(key, DES.MODE_CFB, iv=iv, segment_size=8)

# Perform encryption
 # The actual encryption happens here:
# - DES-CFB processes the plaintext in segments
# - Each segment is XORed with encrypted feedback
    ciphertext = cipher.encrypt(plaintext)

    # Convert ciphertext to UTF-8 hexadecimal
    hex_ciphertext = binascii.hexlify(ciphertext).decode('utf-8')


    with open(ciphertext_path, 'w', encoding='utf-8') as f:
        f.write(hex_ciphertext)

    with open(key_path, 'w') as f:
        f.write(f"Key: {key.hex()}\n")
        f.write(f"IV: {iv.hex()}\n")

    # Print results
    print("\nDES-CFB Encryption Results:")
    print(f"Key: {key.hex()}")
    print(f"IV: {iv.hex()}")
    print("\nCiphertext (UTF-Hex):")
    print(hex_ciphertext)
 

if __name__ == "__main__":
    print("This is Task4-CFB-enc.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")
    main()
