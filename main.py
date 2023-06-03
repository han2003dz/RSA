import math
import random
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def multiplicative_inverse(e, phi):
    x1, x2, y1, y2 = 1, 0, 0, 1
    a, b = e, phi

    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2

    if a == 1:
        return x1 % phi
    else:
        raise ValueError("The multiplicative inverse does not exist")
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    d = multiplicative_inverse(e, phi)
    return e, n, d, n

# hàm mã hóa
def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

# hàm giải mã
def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

# hàm ký
def sign(private_key, message):
    key, n = private_key
    hashed_message = hash_message(message)
    signature = pow(hashed_message, key, n)
    return signature

# hàm xác thực chữ ký
def verify(public_key, message, signature):
    key, n = public_key
    hashed_message = hash_message(message)
    decrypted_signature = pow(signature, key, n)
    return hashed_message == decrypted_signature
# hàm băm
def hash_message(message):
    hash_value = 0
    for char in message:
        hash_value += ord(char)
        hash_value ^= (hash_value << 3) ^ (hash_value >> 2)
    hash_value &= 0xFFFF
    return hash_value

e, n, d, n2 = generate_keypair(31, 41)
print(e, n, d, n2)





