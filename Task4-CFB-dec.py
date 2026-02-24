#KimiaSadatKarbasi-SID60393958
from Crypto.Cipher import DES
import binascii

def main():
    # File paths
    ciphertext_path = '/opt/DES/Task4/cipher.txt' 
    key_path = '/opt/DES/Task4/key.txt'
    decrypted_path = '/opt/DES/Task4/decrypted.txt'

    # Read key and IV (Hex to Binary Conversion)
    try:
        with open(key_path, 'r') as f:
            key = bytes.fromhex(f.readline().split(': ')[1].strip())
            iv = bytes.fromhex(f.readline().split(': ')[1].strip())
    except Exception as e:
        print(f"Error reading key file: {e}")
        return

    # Read ciphertext (Hex to binary Conversion)
    try:
        with open(ciphertext_path, 'r') as f:  # Open in text mode (not 'rb')
            hex_ciphertext = f.read().strip()  # Read hex string
            ciphertext = bytes.fromhex(hex_ciphertext)  # Convert to binary

    except Exception as e:
        print(f"Error reading ciphertext: {e}")
        return

    # Initialize DES-CFB cipher
    cipher = DES.new(key, DES.MODE_CFB, iv=iv, segment_size=8)

    # Decrypt
    decrypted = cipher.decrypt(ciphertext)

    # Write decrypted output
    try:
        with open(decrypted_path, 'wb') as f:
            f.write(decrypted)
        print(f"\nSuccessfully decrypted to: {decrypted_path}")

        # Try to print as text (UTF-8) or hex if binary

        print("\nDecrypted text content:")
        print(decrypted.decode('utf-8'))
        
    except Exception as e:
        print(f"Error writing decrypted file: {e}")

if __name__ == "__main__":
    print("This is Task4-CFB-dec.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")
    main()
