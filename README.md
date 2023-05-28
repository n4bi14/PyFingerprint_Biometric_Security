# Biometric Security Project with PyFingerprint 🔍
## Overview

# Fingerprint Data Encryption and Transmission

This project aims to develop a secure method for storing and transmitting fingerprint data. The project utilizes a Raspberry Pi with a fingerprint sensor to store the fingerprint data securely. The data is then encrypted using hybrid encryption with a symmetric key. The encrypted data is transmitted to a laptop using the CoAP (Constrained Application Protocol) protocol, ensuring secure transmission across the network. Finally, the fingerprint data is decrypted on the laptop and its characteristics are printed.

## Problem/Background

Fingerprint scanners are widely used as a security measure in various environments, such as smartphone authentication and law enforcement applications. It is crucial to ensure that fingerprint data is stored and encrypted properly to prevent unauthorized access to sensitive information. This project explores the complexity of encrypting fingerprint data and its potential implementation in different settings.

## Hardware & Software

- Raspberry Pi with Python
- Breadboard
- Fingerprint Scanner
- CoAP protocol

## Process

1. Use the "pyfingerprint" library and a fingerprint scanner to enroll a new fingerprint on the Raspberry Pi and store the fingerprint data in a text file named "fingerprint_db.txt".
2. Utilize the "cryptography" library to generate a key pair (public + private) on the Raspberry Pi.
3. Encrypt the stored fingerprint characteristics using the hybrid encryption approach and the symmetric key from the previous step.
4. Start a CoAP server on the Raspberry Pi using the "aiocoap" library.
5. Retrieve the encrypted fingerprint data currently stored.
6. Send the encrypted data from the Raspberry Pi to the MacBook using a CoAP GET request.
7. Use Wireshark to verify that only encrypted data is being transmitted across the network.
8. Print the encrypted fingerprint data on the MacBook console.

## Scripts

### Raspberry Pi

- **Enroll_fingerprint.py**: Enrolls new fingerprints and provides the ability to demonstrate fake fingerprints.
- **Generate_key_pair.py**: Creates a public and private key pair.
- **Fingerprint_encrypt_decrypt.py**: Encrypts the fingerprint data using hybrid encryption.
- **CoAP_server.py**: Starts a server, retrieves fingerprint data, encrypts it using a public key, and sends encrypted data upon request.

### MacBook

- **CoAP_client.py**: Sends a request to the Raspberry Pi server to retrieve encrypted fingerprint data, decrypts it, and prints it out.

## Testing/Results

Using the Raspberry Pi, Pyfingerprint, and the Cryptography Python library, we successfully encrypted and decrypted various fingerprints. We also achieved the secure transfer of encrypted prints through CoAP from the Raspberry Pi to a separate system. Wireshark analysis confirmed that the transferred prints contained fully encrypted messages across the computer network.

## Future Work

Given additional time, the following improvements and extensions could be explored:

- Create a more robust fingerprint mold to potentially bypass the fingerprint scanner.
- Develop a local database on the laptop to store all encrypted fingerprint data obtained from the Raspberry Pi. Storing only encrypted files would enhance security.

## References

- GitHub repository: [https://github.com/simedunn/PyFingerprint_Biometric_Security](https://github.com/simedunn/PyFingerprint_Biometric_Security)
- PyFingerprint: [https://pypi.org/project/pyfingerprint/](https://pypi.org/project/pyfingerprint/)
- Aiocoap - Python CoAP library: [https://github.com/chrysn/aiocoap](https://github.com/chrysn/aiocoap)
- Fingerprint mold: [https://www.youtube.com/watch?v=bp-MrrAmprA&ab_channel=JLaservideo](https://www.youtube.com/watch?v=bp-MrrAmprA&ab_channel=JLaservideo)



## Demo 📷
![Encryption/Decryption](assets/images/demo1.png)

Team members:
Simeon Dunn
Abdou Sidiya
Nabila Abdoulkadri
Karen Bonilla




----
## Teammates 💪
<a href="https://github.com/simedunn/PyFingerprint_Biometric_Security/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=simedunn/PyFingerprint_Biometric_Security" />
</a>
