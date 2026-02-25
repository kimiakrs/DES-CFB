# Implementation of DES in CFB Mode using Python and OpenSSL

This project presents a complete implementation of the Data Encryption Standard (DES) in Cipher Feedback (CFB) mode using Python (PyCryptodome library) and a comparative integration with OpenSSL.

The study demonstrates encryption, decryption, verification, and performance comparison between a custom Python-based implementation and OpenSSL’s optimized DES-CFB.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![PyCryptodome](https://img.shields.io/badge/Library-PyCryptodome-green.svg)](https://pycryptodome.readthedocs.io/)
[![OpenSSL](https://img.shields.io/badge/OpenSSL-v3.x-lightgrey.svg)](https://www.openssl.org/)
[![DES](https://img.shields.io/badge/Algorithm-DES-red.svg)](https://en.wikipedia.org/wiki/Data_Encryption_Standard)
[![CFB Mode](https://img.shields.io/badge/Mode-CFB%20Mode-purple.svg)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_feedback_(CFB))
[![Cryptography](https://img.shields.io/badge/Field-Cryptography-darkblue.svg)](https://en.wikipedia.org/wiki/Cryptography)
[![Security](https://img.shields.io/badge/Focus-Security-critical.svg)](https://en.wikipedia.org/wiki/Computer_security)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---
## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Phase1: DES Encryption (PyCryptodome)](#phase1-des-encryption-cfb-mode)
- [Phase2: DES Decryption (PyCryptodome)](#phase2-des-decryption-cfb-mode)
- [Phase3: OpenSSL Integration](#phase3-openssl-integration)
- [Phase4: Comparative Analysis](#phase4-comparative-analysis)
- [Project Structure](#project-structure)
- [Key Learning Outcomes](#key-learning-outcomes)
- [License](#license)

---

## Project Overview

The project is structured into four main phases:

1. DES Encryption in CFB Mode (Python - PyCryptodome)
2. DES Decryption in CFB Mode
3. OpenSSL-based DES-CFB Encryption & Decryption
4. Comparative Analysis (Performance, Security, Design)

---

## Technologies Used

| Component | Description |
|-----------|------------|
| Python 3.x | Programming language used for implementation |
| PyCryptodome | Cryptographic library for DES encryption/decryption |
| OpenSSL (v3.x) | External tool for DES-CFB encryption and verification |
| Legacy Provider | Required in OpenSSL v3+ to enable DES support |
| Linux Environment | Execution environment for development and testing |
---

## Installation

Install required Python library:

```bash
pip install pycryptodome
```
---

## Phase1: DES Encryption (CFB Mode)

**Steps:**

1. Import required cryptographic modules

2. Read plaintext input file

3. Generate:

* 64-bit DES Key
* 64-bit Initialization Vector (IV)

4. Configure DES in CFB Mode:


```python
cipher = DES.new(key, DES.MODE_CFB, iv=iv, segment_size=8)

```

---

## Phase2: DES Decryption (CFB Mode)

**Steps:**

1. Read chipher text
2. Read stored Key and IV
3. Reintialize DES cipher
4. Decrypt ciphertext

```
decrypted = cipher.decrypt(ciphertext)

```

---

## Phase3: OpenSSL Integration

1. Encryption Command (CFB Mode)


```
openssl enc -des-cfb -K <key_hex> -iv <iv_hex> -provider legacy

```

2. Decryption Command


```
openssl enc -d -des-cfb -K <key_hex> -iv <iv_hex> -provider legacy
```

*The OpenSSL execution is automated via Python using the subprocess module.*


---

## Phase4: Comparative Analysis 

The project compares: 

### Implementation & Design

| Aspect       | Custom DES-CFB                 | OpenSSL DES-CFB                |
| ------------ | ------------------------------ | ------------------------------ |
| Codebase     | Python (manual implementation) | Precompiled binary             |
| Mode Support | Manual CFB logic               | Built-in `-des-cfb`            |
| Provider     | N/A                            | Requires legacy provider (v3+) |


### Performance & Optimization

| Aspect                | Custom DES-CFB              | OpenSSL DES-CFB                     |
| --------------------- | --------------------------- | ----------------------------------- |
| Speed                 | Slower (Python interpreter) | Faster (optimized C implementation) |
| Hardware Acceleration | No                          | Uses CPU optimizations              |


### Security

| Aspect                  | Custom DES-CFB | OpenSSL DES-CFB   |
| ----------------------- | -------------- | ----------------- |
| Side-Channel Protection | Limited        | Hardened          |
| Padding                 | Manual         | Automatic         |
| Maintenance             | Manual         | Regularly updated |


---

## Project Structure 
```
DES-CFB/
│
├── Task4-CFB-enc.py
├── Task4-CFB-dec.py
├── Task4-CFB-openssl.py
├── Report-Task4.pdf
```

**The complete step-by-step implementation, execution workflow, screenshots, and comparative analysis are documented in the full project report [Report-Task4.pdf](/Report-Task4.pdf)**

### Execution Workflow

Run encryption:
```python
python3 Task4-CFB-enc.py
```
Run decryption:
```python
python3 Task4-CFB-dec.py
```
Run Openssl operation:
```python
Task4-CFB-Openssl.py
```
---

## Key Learning Outcomes

* Understanding block cipher modes of operation

* Implementing symmetric encryption using PyCryptodome

* Handling key and IV management securely

* Integrating OpenSSL commands via Python

* Comparing custom cryptographic implementations with production-grade tools

* Observing performance and security trade-offs


**DES is considered cryptographically weak and should not be used in modern production systems. This implementation is strictly for educational and academic purposes.**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

