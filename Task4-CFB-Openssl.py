#KimiaSadatKarbasi-SID60393958
#Using this for the Linux command
import subprocess


# File paths
PLAINTEXT_PATH = '/opt/DES/Task4/plain.txt'
KEY_PATH = '/opt/DES/Task4/key.txt'
CIPHERTEXT_PATH = '/opt/DES/Task4/cipher.txt'
CIPHERTEXT_OPENSSL_PATH = '/opt/DES/Task4/cipher-openssl.txt'
DECRYPTED_OPENSSL_PATH = '/opt/DES/Task4/decrypted-openssl.txt'

def openssl_des_cfb():
    #Read Key and IV from the text
    with open(KEY_PATH, 'r') as f:
        key_hex = f.readline().split(': ')[1].strip()  
        iv_hex = f.readline().split(': ')[1].strip()  

    #Read plaintext in binary mode
    with open(PLAINTEXT_PATH, 'rb') as f:
        plaintext = f.read()

    # Encrypt with OpenSSL (DES-CFB)
    openssl_cmd = [
        'openssl', 'enc', '-des-cfb',  #CFB mode
        '-K', key_hex,               
        '-iv', iv_hex,

        #For using CFB mode in Openssl we need legacy provider                
        '-provider', 'legacy'       
    ]

    result = subprocess.run(
        openssl_cmd,
        input=plaintext,
        capture_output=True,
        check=True
    )

    # Save OpenSSL ciphertext in hex format
    ciphertext_hex = result.stdout.hex()
    with open(CIPHERTEXT_OPENSSL_PATH, 'w') as f:
        f.write(ciphertext_hex)

    # Read DES ciphertext (hex format)
    with open(CIPHERTEXT_PATH, 'r') as f:
        des_ciphertext_hex = f.read().strip()

    # Decrypt with OpenSSL (verify)
    openssl_decrypt_cmd = [
        'openssl', 'enc', '-d', '-des-cfb8',
        '-K', key_hex,
        '-iv', iv_hex,
        '-provider', 'legacy'
    ]

    # Convert hex ciphertext to binary for decryption
    ciphertext_bin = bytes.fromhex(ciphertext_hex)
    result_decrypt = subprocess.run(
        openssl_decrypt_cmd,
        input=ciphertext_bin,
        capture_output=True,
        check=True
    )

    # Save decrypted output
    with open(DECRYPTED_OPENSSL_PATH, 'wb') as f:
        f.write(result_decrypt.stdout)


    # Compare hex ciphertexts
    print("\nOpenSSL (DES-CFB) Results")
    print(f"Key: {key_hex}")
    print(f"IV: {iv_hex}")
    print(f"OpenSSL Ciphertext (first 32 chars): {ciphertext_hex[:32]}")
    print(f"DES Ciphertext (first 32 chars): {des_ciphertext_hex[:32]}")
    print(f"Ciphertexts match: {ciphertext_hex == des_ciphertext_hex}")
    print(f"\nDecrypted matches original: {result_decrypt.stdout == plaintext}")

if __name__ == "__main__":
    print("This is Task4-CFB-openssl.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")
    openssl_des_cfb()