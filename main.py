import random
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
# e, n, d, n2 = generate_keypair(31, 41)
# print(e, n, d, n2)