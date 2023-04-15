from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# generate a private key
private_key = rsa.generate_private_key(
    
    public_exponent=65537,
    key_size=2048
)

# get the public key from the private key
public_key = private_key.public_key()

# serialize the public key 
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# write the public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(public_key_bytes)
    
    
# serialize the private key
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save the serialized private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_key_bytes)


